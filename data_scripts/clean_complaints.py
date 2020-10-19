from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
from pyspark.sql.functions import from_utc_timestamp
import json
import pandas as pd
import janitor.spark
import time

# Load the configuration s3file
with open("config.json") as config_json:
    config = json.load(config_json)

# Data Config
region = 'us-west-1'
bucket = config['s3']['bucket']
# Update to iterate over the 65 listings csv's; append to postgre
key = 'NYC_Full_311.csv'
# key = 'NYC311_1k.csv'
# key = 'call10k.csv'


sc = SparkContext()
sc._jsc.hadoopConfiguration().set('fs.s3a.endpoint', f's3-{region}.amazonaws.com')

spark = SparkSession(sc)

# Postgres Config
url = f"jdbc:postgresql://{config['postgre']['ip']}:{config['postgre']['port']}/{config['postgre']['db']}"
properties = {"user": config['postgre']['user'],
              "password": config['postgre']['password'],
              "driver": "org.postgresql.Driver"}

# Read 311 Data from S3
s3file = f's3a://{bucket}/{key}'
raw_df = spark.read.csv(s3file, header = True, inferSchema=True, multiLine=True, escape='"')

# Read csv containing complaints mapping to broader topics
topics_key = 'unique_complaints.csv'
topics_s3file = f's3a://{bucket}/{topics_key}'
topics_raw_df = spark.read.csv(topics_s3file, header = True, inferSchema=True, escape='"')

# Convert complaint_type column to lowercase
raw_df = raw_df.withColumn('Complaint Type', lower(col('Complaint Type')))
raw_df = raw_df.withColumn('Descriptor', lower(col('Descriptor')))

columns = ['Created Date', 'Complaint Type', 'Descriptor', 'Incident Zip', 'Latitude', 'Longitude', 'Borough']

t1 = time.time()
# Select certain columns
complaint_selected = raw_df.select(columns)
# complaint_selected.show(10)

# Join the 311 complaints with the mapping to complaint topics
complaints_joined = complaint_selected.join(topics_raw_df, "Complaint Type")
# complaints_joined.show(10)


# Filter for only Brooklyn and make the Borough column lowercase
# complaints_joined = complaints_joined.filter(complaints_joined['Borough'] == 'BROOKLYN')
complaints_joined = complaints_joined.where(F.col('Incident Zip').isin({"10002", "10003", "10009"}))
# complaints_joined = complaints_joined.drop(col('Borough'))
# complaints_joined = complaints_joined.withColumn('Borough', lit('MANHATTAN'))
complaints_joined = complaints_joined.withColumn("Borough", lit('MANHATTAN'))
complaints_joined = complaints_joined.withColumn('Borough', lower(col('Borough')))
complaints_joined.show()
# TEST: check number of nan in Clean_Complaint
# complaints_joined.select([count(when(isnan(c), c)).alias(c) for c in complaints_joined.columns]).show()

#Set the datatypes for the columns
complaints_joined = complaints_joined.withColumn('Created Date', to_timestamp('Created Date',
                                                 format='MM/dd/yyyy hh:mm:ss aa'))

complaints_joined = complaints_joined.withColumn('month', F.month('Created Date'))
complaints_joined = complaints_joined.withColumn('year', F.year('Created Date'))
complaints_joined = complaints_joined.withColumn('Incident Zip',
                                                 complaints_joined["Incident Zip"].cast(IntegerType()))
complaints_joined = complaints_joined.withColumn('Latitude', col('Latitude').cast('float'))
complaints_joined = complaints_joined.withColumn('Longitude', col('Longitude').cast('float'))

# Filter anything before 2015
complaints_joined = complaints_joined.filter(complaints_joined['year'] >= 2020)

# Reove any complaints with no location information
complaints_joined = complaints_joined.filter(complaints_joined['latitude'].isNotNull() &
                                             complaints_joined['longitude'].isNotNull())
complaints_joined = complaints_joined.filter(complaints_joined['Clean_Complaint'].isNotNull())

# Rename columns
complaints_joined = complaints_joined.clean_names()
complaints_joined.show()
# Add to database

complaints_joined.write.jdbc(url, table="complaints_2020", mode="append", properties=properties)
t2 = time.time()
outfile = open("clean_complaints_writetime.txt", 'w')
outfile.write(str(t2-t1))
outfile.close()

print ("It took ", t2-t1, " seconds to clean complaint data.")

spark.stop()
