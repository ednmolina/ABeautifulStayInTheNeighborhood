from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
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

# Read dataset
sql_query = """select
l.listing_id,
l.latitude,
l.longitude,
l.neighbourhood_cleansed,
l.neighbourhood_group_cleansed,
l.price,
l.bedrooms,
l.bathrooms,
l.minimum_nights,
l.timestamp,
l.number_of_reviews,
l.month,
l.year,
l.avg_30_price,
l.geom,
l.circle
from listings l
inner join (
select max(number_of_reviews), listing_id
from listings
group by (listing_id, year)
order by max(number_of_reviews)
desc limit 1000 ) b
on l.listing_id = b.listing_id
and number_of_reviews = number_of_reviews"""

top_listings_df = spark.read.format("jdbc") \
                        .option("url", url) \
                        .option("query", sql_query) \
                        .option("user" , properties['user']) \
                        .option("password" , properties['password']) \
                        .option("driver", properties['driver']) \
                        .load()

top_listings_df.show()
# Save to database
t1 = time.time()
top_listings_df.write.jdbc(url, table="top_listings", mode="append", properties=properties)
t2 = time.time()

outfile = open("top_listings_writetime.txt", 'w')
outfile.write(str(t2-t1))
outfile.close()
print (str(t2-t1))

spark.stop()
