from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
import json

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

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
import json

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
complaints_df = spark.write.format("jdbc") \
                        .option("url", url) \
                        .option("query", "CREATE TABLE test as (select * from complaints limit 10)") \
                        .option("user" , properties['user']) \
                        .option("password" , properties['password']) \
                        .option("driver", properties['driver']) \
                        .load()
complaints_df.show()
# listings_df.show()
# # Create tempview to query
# # listings_df.createOrReplaceTempView('listings')
# #
# # # Test query
# # listings_query = spark.sql("""
# #     SELECT latitude, longitude
# #     FROM listings
# #     LIMIT 10
# # """)
# # listings_query.show()
#
spark.stop()
