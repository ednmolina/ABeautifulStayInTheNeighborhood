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
                    .config("spark.executor.heartbeatInterval", "12000s")\
                    .config("spark.network.timeout", "600s")\
                    .getOrCreate()

# Read dataset
sql_query = """"""

nearest_complaints_df = spark.read.format("jdbc") \
                        .option("url", url) \
                        .option("query", sql_query) \
                        .option("user" , properties['user']) \
                        .option("password" , properties['password']) \
                        .option("driver", properties['driver']) \
                        .load()



spark.stop()
