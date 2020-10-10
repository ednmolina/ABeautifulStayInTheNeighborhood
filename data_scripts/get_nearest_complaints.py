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
                    # .config("spark.executor.heartbeatInterval", "12000s")\
                    # .config("spark.network.timeout", "11000s")\


# # Read listings data
# listings_df = spark.read.jdbc(url=url, table='listings', properties=properties)
#
# # Create tempview to query
# listings_df.createOrReplaceTempView('listings')
#
# # Test query
# listings_query = spark.sql("""
#     SELECT latitude, longitude
#     FROM listings
#     LIMIT 10
# """)
# listings_query.show()


# #Read listings data
# complaints_df = spark.read.jdbc(url=url, table='complaints', properties=properties)
#
# # Create tempview to query
# complaints_df.createOrReplaceTempView('complaints')

# Test query
# complaints_query = spark.sql("""
#     select * from complaints limit 10
# """)
# complaints_query.show()
# spark.stop()

"""NEW METHOD"""

# Read dataset
sql_query = """select
    c.latitude lat_comp,
    c.longitude long_comp,
    c.created_date,
    c.clean_complaint,
    c.complaint_type,
    c.descriptor,
    c.incident_zip,
    l.listing_id,
    l.latitude lat_list,
    l.longitude long_list,
    l.neighbourhood_cleansed,
    l.neighbourhood_group_cleansed,
    l.timestamp,
    ST_Distance(c.geom, l.geom) as distance
from complaints c, listings l
where ST_Intersects(ST_Buffer(c.geom, 100), l.circle)"""

nearest_complaints_df = spark.read.format("jdbc") \
                        .option("url", url) \
                        .option("query", sql_query) \
                        .option("user" , properties['user']) \
                        .option("password" , properties['password']) \
                        .option("driver", properties['driver']) \
                        .load()

nearest_complaints_df.show()
# Save to database
t1 = time.time()
nearest_complaints_df.write.jdbc(url, table="nearest_complaints", mode="append", properties=properties)
t2 = time.time()

outfile = open("nearest_complaints_writetime.txt", 'w')
outfile.write(t2-t1)
outfile.close()
print (t2-t1)

spark.stop()
