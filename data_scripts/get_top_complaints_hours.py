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

# Postgres Config
url = f"jdbc:postgresql://{config['postgre']['ip']}:{config['postgre']['port']}/{config['postgre']['db']}"
properties = {"user": config['postgre']['user'],
              "password": config['postgre']['password'],
              "driver": "org.postgresql.Driver"}

spark = SparkSession.builder \
                    .appName("ABSIN") \
                    .getOrCreate()

# QUery mode of complaints for each listing and when complaints are reported
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
nearest_complaints_df.show()

# Get the top complaint for each listing
complaints_count = nearest_complaints_df.groupBy('listing_id', 'clean_complaint').count()
complaints_count.registerTempTable('complaints_count')
top_complaints = spark.sql("""select * from (
    select listing_id,
           clean_complaint,
           row_number() over (partition by listing_id order by count desc) as rank
    from complaints_count) ranks where rank <= 1""")
top_complaints = top_complaints.drop(col('rank'))
top_complaints.show()

# Get the top hour each complaint is reported for each listing
listing_hours = nearest_complaints_df.select(['listing_id', 'created_date']).withColumn('hour', hour(col('created_date')))
hours_count = listing_hours.groupBy('listing_id', 'hour').count()
hours_count.registerTempTable('hours_count')
top_hours = spark.sql("""select * from (
    select listing_id,
           hour,
           row_number() over (partition by listing_id order by count desc) as rank
    from hours_count) ranks where rank <= 1""")
top_hours = top_hours.orderBy(col('listing_id')).drop(col('rank'))
top_hours.show()

# Save to database
t1 = time.time()
top_complaints.write.jdbc(url, table="top_complaints", mode="append", properties=properties)
t2 = time.time()

t3 = time.time()
top_hours.write.jdbc(url, table="top_hours", mode="append", properties=properties)
t4 = time.time()

outfile = open("top_complaints_hours_LowerEastSide_Oct14.txt", 'w')
outfile.write('%s, %s'%(str(t2-t1), str(t4-t3)))
outfile.close()
print (t2-t1, t4-t3)
spark.stop()
