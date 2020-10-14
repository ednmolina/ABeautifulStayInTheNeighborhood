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
                distinct(listing_id),
                latitude,
                longitude,
                geom,
                circle
               from listings"""

unique_listing_ids_df = spark.read.format("jdbc") \
                                  .option("url", url) \
                                  .option("query", sql_query) \
                                  .option("user" , properties['user']) \
                                  .option("password" , properties['password']) \
                                  .option("driver", properties['driver']) \
                                  .load()

unique_listing_ids_df = unique_listing_ids_df.withColumn('timestamp', to_timestamp("timestamp"))
unique_listing_ids_df = unique_listing_ids_df.withColumn('month', F.month('timestamp'))
unique_listing_ids_df = unique_listing_ids_df.withColumn('year', F.year('timestamp'))

unique_listing_ids_df.show(2)
t1 = time.time()
unique_listing_ids_df.write.jdbc(url, table="unique_listings", mode="append", properties=properties)
t2 = time.time()

outfile = open("unique_listing_ids_writetime.txt", 'w')
outfile.write(str(t2-t1))
outfile.close()
print (t2-t1)

spark.stop()
