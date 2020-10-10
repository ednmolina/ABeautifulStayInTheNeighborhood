from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
import json
import time
import pandas as pd
import numpy as np

# Load the configuration s3file
with open("config.json") as config_json:
    config = json.load(config_json)

# Data Config
region = 'us-west-1'
bucket = config['s3']['bucket']

# Spark
sc = SparkContext()
sc._jsc.hadoopConfiguration().set('fs.s3a.endpoint', f's3-{region}.amazonaws.com')
# sc.setLogLevel("ERROR")
spark = SparkSession(sc)

# Postgres Config
url = f"jdbc:postgresql://{config['postgre']['ip']}:{config['postgre']['port']}/{config['postgre']['db']}"
properties = {"user": config['postgre']['user'],
              "password": config['postgre']['password'],
              "driver": "org.postgresql.Driver"}

# Load the csv containing files to load from s3 containing Airbnb Data
abnb_files = pd.read_csv('files_to_read.csv')

# Remove dollar from printSchema
get_price = udf(lambda x: float(x.replace('$', '').replace(',', '')), FloatType())

t1 = time.time()

for i in range(abnb_files.shape[0]):

    listing_key = abnb_files['listing'][i]
    calendar_key = abnb_files['calendar'][i]

    listing_s3file = f's3a://{bucket}/{listing_key}'
    calendar_s3file = f's3a://{bucket}/{calendar_key}'
    print ("Working on: ", listing_s3file)
    listing_raw_df = raw_df = spark.read.csv(listing_s3file,
                                             header = True,
                                             inferSchema=True,
                                             escape='"',
                                             multiLine = True)

    calendar_raw_df = raw_df = spark.read.csv(calendar_s3file,
                                              header = True,
                                              inferSchema=True,
                                              escape='"',
                                              multiLine = True)

    # Subset the listing and calendar dataframes
    listing_cols = ['id', 'latitude', 'longitude', 'neighbourhood_cleansed',
                    'neighbourhood_group_cleansed', 'price', 'bedrooms',
                    'bathrooms', 'minimum_nights', 'last_scraped']
    calendar_cols = ['listing_id', 'date', 'available', 'price']

    listings_selected = listing_raw_df[listing_cols]

    # Rename columns, and add month and year columns
    listings_selected = listings_selected.withColumnRenamed('id', 'listing_id')
    listings_selected = listings_selected.withColumnRenamed('last_scraped', 'timestamp')
    listings_selected = listings_selected.withColumn('timestamp', to_timestamp("timestamp"))
    listings_selected = listings_selected.withColumn('month', F.month('timestamp'))
    listings_selected = listings_selected.withColumn('year', F.year('timestamp'))

    calendar_selected = calendar_raw_df[calendar_cols]

    # Compute the monthly average per listing from calendar_selected dataframes
    # Remove null, remove dollarsign, then group by listing and compute monthly average
    calendar_price = calendar_raw_df[['listing_id', 'price']].filter(calendar_selected['price'].isNotNull())
    calendar_price = calendar_price.withColumn('price', get_price(calendar_price['price']))

    calendar_averaged = calendar_price.groupBy('listing_id').agg(avg(col("price")))
    calendar_averaged = calendar_averaged.withColumnRenamed('avg(price)', 'avg_30_price')

    # Join the listing data with the 30_dy average data; will no inner join now
    listings_joined = listings_selected.join(calendar_averaged, "listing_id")


    # Drop where lat, long are null
    listings_joined = listings_joined.filter(listings_joined['latitude'].isNotNull() &
                                             listings_joined['longitude'].isNotNull())
    listings_selected.show()
    listings_joined.write.jdbc(url, table="listings", mode="append", properties=properties)
t2 = time.time()


outfile = open("clean_airbnb_writetime.txt", 'w')
outfile.write(t2-t1)
outfile.close()

spark.stop()
# Append to the table
 # df.write.jdbc(url, table="abb", mode="append", properties=props)
