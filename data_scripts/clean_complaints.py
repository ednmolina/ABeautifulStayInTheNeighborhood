from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
import json
import pandas as pd

# Load the configuration s3file
with open("config.json") as config_json:
    config = json.load(config_json)

# Data Config
region = 'us-west-1'
bucket = config['s3']['bucket']
# Update to iterate over the 65 listings csv's; append to postgre
key = 'NYC_Full_311.csv'
# key = 'NYC311_1k.csv'
key = 'call10k.csv'


sc = SparkContext()
sc._jsc.hadoopConfiguration().set('fs.s3a.endpoint', f's3-{region}.amazonaws.com')

spark = SparkSession(sc)

# Postgres Config
url = f"jdbc:postgresql://{config['postgre']['ip']}:{config['postgre']['port']}/{config['postgre']['db']}"
properties = {"user": config['postgre']['user'],
              "password": config['postgre']['password'],
              "driver": "org.postgresql.Driver"}

# Read Data from S3
s3file = f's3a://{bucket}/{key}'
raw_df = spark.read.csv(s3file, header = True, inferSchema=True, multiLine=True, escape='"')

raw_df.show()
"""

# Convert complaint_type column to lowercase
complaint_column = 'Complaint Type'
# complaint_column = 'complaint_type'
raw_df = raw_df.withColumn(complaint_column, lower(col(complaint_column)))

columns = ['Created Date', 'Complaint Type', 'Incident Zip', 'Latitude', 'Longitude']
# columns = ['created_date', 'complaint_type', 'incident_zip', 'latitude', 'longitude']

# Select certain columns
df_selected = raw_df.select(columns)

# Filter out non-complaints
# df_selected = df_selected.filter((~df_selected[complaint_column].contains('comments'))
#                                 &(~df_selected[complaint_column].contains(".."))
#                                 &(~df_selected[complaint_column].contains("sg-9"))
#                                 &(~df_selected[complaint_column].contains("trans fat"))
#                                 &(~df_selected[complaint_column].contains("forms"))
#                                 &(~df_selected[complaint_column].contains("question"))
#                                 &(~df_selected[complaint_column].contains('web-inf'))
#                                 &(~df_selected[complaint_column].contains('%c'))
#                                 &(~df_selected[complaint_column].contains('ztestint'))
#                                 &(~df_selected[complaint_column].contains('%2'))
#                                 &(~df_selected[complaint_column].contains('qf'))
#                                 &(~df_selected[complaint_column].contains('.php'))
#                                 &(~df_selected[complaint_column].contains('passwd'))
#                                 &(~df_selected[complaint_column].contains("c:"))
#                                 &(~df_selected[complaint_column].contains('passwd'))
#                                 &(~df_selected[complaint_column].contains('='))
#                                 &(~df_selected[complaint_column].contains('dca'))
#                                 &(~df_selected[complaint_column].contains('.xml'))
#                                 &(~df_selected[complaint_column].contains('{ :;}'))
#                                 &(~df_selected[complaint_column].contains('*'))
#                                 &(~df_selected[complaint_column].contains(';'))
#                                 &(~df_selected[complaint_column].contains('general'))
#                                 &(~df_selected[complaint_column].contains('dire'))
#                                 &(~df_selected[complaint_column].contains('ferry permit'))
#                                 &(~df_selected[complaint_column].contains('sleep 11')))
# Get the unique complaits
unique_complaints = df_selected.select(complaint_column).distinct()

# Sort alphabetically
counted_complaints = counted_complaints.sort(complaint_column)
counted_complaints.toPandas().to_csv('unique_complaints_2.csv', index=False)
# filtered_complaints = counted_complaints.filter(counted_complaints['count']>=1)

# Create new column with generalized complaint_types
# complaints_replaced = filtered_complaints.withColumn("complaint",
#                         expr("case when complaint_type contains 'noise' then 'NOISE'""+
#                              "else 'OTHER' end"))
# complaints_replaced = filtered_complaints.withColumn("complaint",
#                                                      F.when(col(complaint_column).contains('noise'), 'Noise')
#                                                      .when(col(complaint_column).contains('fireworks'), 'Noise')
#                                                      .when(col(complaint_column).contains('construction'), 'Noise')
#                                                      .when(col(complaint_column).contains('water'), 'Water and Power')
#                                                      .when(col(complaint_column).contains('cooling tower'), 'Water and Power')
#                                                      .when(col(complaint_column).contains('boiler'), 'Water and Power')
#                                                      .when(col(complaint_column).contains('sprinkler'), 'Water and Power')
#                                                      .when(col(complaint_column).contains('plumbing'), 'Water and Power')
#                                                      .when(col(complaint_column).contains('leak'), 'Water and Power')
#                                                      .when(col(complaint_column).contains('homeless'), 'Homeless')
#                                                      .when(col(complaint_column).contains('structural'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('flooring'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('appliance'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('fire alarm'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('paint'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('public toilet'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('bike rack'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('non-residential heat'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('scaffold'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('electric'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('stairs'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('window'), 'Building Infrastructure')
#                                                      .when(col(complaint_column).contains('parking'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('vehicle'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('bus'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('payphone'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('stalled sites'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('parking meter'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('derelict'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('driveway'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('abandoned vehicle'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('curb'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('panhandeling'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('food vendor'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('streetlight'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('recycling'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('street light'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('sidewalk'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('street'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('traffic signal'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('taxi'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('sweeping'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('transportation'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('waste'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('highway'), 'Parking and Street')
#                                                      .when(col(complaint_column).contains('drug'), 'Health')
#                                                      .when(col(complaint_column).contains('hazard'), 'Health')
#                                                      .when(col(complaint_column).contains('unsanitary'), 'Health')
#                                                      .when(col(complaint_column).contains('sanitation'), 'Health')
#                                                      .when(col(complaint_column).contains('mosquitos'), 'Health')
#                                                      .when(col(complaint_column).contains('asbestos'), 'Health')
#                                                      .when(col(complaint_column).contains('mold'), 'Health')
#                                                      .when(col(complaint_column).contains('sewer'), 'Health')
#                                                      .when(col(complaint_column).contains('air quality'), 'Health')
#                                                      .when(col(complaint_column).contains('smoking'), 'Health')
#                                                      .when(col(complaint_column).contains('lead'), 'Health')
#                                                      .when(col(complaint_column).contains('health'), 'Health')
#                                                      .when(col(complaint_column).contains('covid'), 'Health')
#                                                      .when(col(complaint_column).contains('gas'), 'Health')
#                                                      .when(col(complaint_column).contains('industrial waste'), 'Health')
#                                                      .when(col(complaint_column).contains('food poisoning'), 'Health')
#                                                      .when(col(complaint_column).contains('hazmat'), 'Health')
#                                                      .when(col(complaint_column).contains('radioactive'), 'Health')
#                                                      .when(col(complaint_column).contains('bees'), 'Health')
#                                                      .when(col(complaint_column).contains('dirty'), 'Health')
#                                                      .when(col(complaint_column).contains('urinating'), 'Health')
#                                                      .when(col(complaint_column).contains('animal'), 'Animal')
#                                                      .when(col(complaint_column).contains('trapping pigeon'), 'Animal')
#                                                      .when(col(complaint_column).contains('unlicensed dog'), 'Animal')
#                                                      .when(col(complaint_column).contains('pet'), 'Animal')
#                                                      .when(col(complaint_column).contains('dog'), 'Animal')
#                                                      .when(col(complaint_column).contains('cat'), 'Animal')
#                                                      .when(col(complaint_column).contains('rodent'), 'Animal')
#                                                      .when(col(complaint_column).contains('litter basket'), 'Animal')
#                                                      .when(col(complaint_column).contains('illegal tree'), 'Plant')
#                                                      .when(col(complaint_column).contains('plant'), 'Plant')
#                                                      .when(col(complaint_column).contains('xmas tree'), 'Plant')
#                                                      .when(col(complaint_column).contains('dead/dying tree'), 'Plant')
#                                                      .when(col(complaint_column).contains('tree'), 'Plant')
#                                                      .when(col(complaint_column).contains('home deliverey'), 'Meal Delivery')
#                                                      .when(col(complaint_column).contains('home delivered'), 'Meal Delivery')
#                                                      .otherwise('Other'))
# # complaints_replaced.show(2000)
# complaints_replaced.write.save(f's3a://{bucket}/complaints.csv', format = 'csv', header = True)



# Count unique values
# df_selected.count()
# unique_counts = df_selected.select(countDistinct('id'))
# unique_counts.show()
# df_selected.groupBy('id').count().show()
# df_selected.groupBy(['latitude', 'longitude']).count().show()
# df_selected.show()
# df_selected.printSchema()
"""
spark.stop()
# Append to the table
 # df.write.jdbc(url, table="abb", mode="append", properties=props)
