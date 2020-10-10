from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
import json
import pandas as pd
import janitor.spark

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

# Read csv containing zip code and borough
zip_key = 'zip_borough.csv'
zip_s3file = f's3a://{bucket}/{topics_key}'
zip_raw_df = spark.read.csv(topics_s3file, header = True, inferSchema=True, escape='"')
zip_raw_df.show()
