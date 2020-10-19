from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.sql import functions as F
import pyspark.sql.functions as psf
import json
import time

from sqlalchemy import Table, Column, Integer, Float, String, MetaData, create_engine
from geoalchemy2 import Geography
from sqlalchemy.sql import select
from sqlalchemy import func

# Load the configuration s3file
with open("config.json") as config_json:
    config = json.load(config_json)

# # Postgres Config
url = f"jdbc:postgresql://{config['postgre']['ip']}:{config['postgre']['port']}/{config['postgre']['db']}"
properties = {"user": config['postgre']['user'],
              "password": config['postgre']['password'],
              "driver": "org.postgresql.Driver"}


spark = SparkSession.builder \
                    .appName("ABSIN") \
                    .getOrCreate()
                    # .config("spark.executor.heartbeatInterval", "12000s")\
                    # .config("spark.network.timeout", "11000s")\

# Using ST_Intersects query nearest complaints
sql_query = """select
    c.created_date,
    c.clean_complaint,
	l.listing_id,
    l.latitude lat_list,
    l.longitude long_list,
	l.price,
	l.bedrooms,
	l.bathrooms,
	l.avg_30_price,
    l.month,
    l.year,
	l.minimum_nights,
	l.neighbourhood_cleansed,
    l.neighbourhood_group_cleansed,
    l.listing_url,
    l.number_of_reviews
from complaints_2020 c inner join listings_2020 l
on ST_Intersects(c.circle, l.circle)
where l.neighbourhood_group_cleansed = 'Manhattan'
and l.neighbourhood_cleansed = 'Lower East Side'
and c.month = 8
and c.year = 2020"""


nearest_complaints_df = spark.read.format("jdbc") \
                        .option("url", url) \
                        .option("query", sql_query) \
                        .option("user" , properties['user']) \
                        .option("password" , properties['password']) \
                        .option("driver", properties['driver']) \
                        .load()

# Get all the unique listings in Williamsburg, Brooklyn
unique_listings = nearest_complaints_df.drop_duplicates(['listing_id']).drop('clean_complaint')

# Reformat the price column to remove the dollar sign
get_price = udf(lambda x: float(x.replace('$', '').replace(',', '')), FloatType())
unique_listings = unique_listings.withColumn('price', get_price(unique_listings['price']))
unique_listings.show()

# Save to database
t1 = time.time()
unique_listings.write.jdbc(url, table="nearest_complaints_STDistance", mode="append", properties=properties)
t2 = time.time()

outfile = open("nearest_complaints_writetime_STDistance_Williamsburg_Oct15.txt", 'w')
outfile.write(str(t2-t1))
outfile.close()
print (str(t2-t1))

spark.stop()
