from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
import json

# Load the configuration s3file
with open("config.json") as config_json:
    config = json.load(config_json)

# Data Config
region = 'us-west-1'
bucket = config['s3']['bucket']
# Update to iterate over the 65 listings csv's; append to postgre
# key = 'NYC_Full_311.csv'
key = 'NYC311_1k.csv'

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

# Convert complaint_type column to lowercase
raw_df = raw_df.withColumn('complaint_type', lower(col('complaint_type')))

# columns = ['Created Date', 'Complaint Type', 'Incident Zip', 'Latitude', 'Longitude']
columns = ['created_date', 'complaint_type', 'incident_zip', 'latitude', 'longitude']

# Select certain columns
df_selected = raw_df.select(columns)

# Get the unique complaits
unique_complaints = df_selected.select('complaint_type').distinct()

# Count and fitler
counted_complaints = unique_complaints.groupBy("complaint_type").count()
filtered_complaints = counted_complaints.filter(counted_complaints['count']>=1)
filtered_complaints.show(2000)

# Create new column with generalized complaint_types
# complaints_replaced = filtered_complaints.withColumn("complaint",
#                         expr("case when complaint_type contains 'noise' then 'NOISE'""+
#                              "else 'OTHER' end"))
complaints_replaced = filtered_complaints.withColumn("complaint",
                                                     F.when(col('complaint_type').contains('noise'), 'Noise')
                                                     .when(col('complaint_type').contains('fireworks'), 'Noise')
                                                     .when(col('complaint_type').contains('construction'), 'Noise')
                                                     .when(col('complaint_type').contains('water'), 'Water and Power')
                                                     .when(col('complaint_type').contains('cooling tower'), 'Water and Power')
                                                     .when(col('complaint_type').contains('boiler'), 'Water and Power')
                                                     .when(col('complaint_type').contains('sprinkler'), 'Water and Power')
                                                     .when(col('complaint_type').contains('plumbing'), 'Water and Power')
                                                     .when(col('complaint_type').contains('leak'), 'Water and Power')
                                                     .when(col('complaint_type').contains('homeless'), 'Homeless')
                                                     .when(col('complaint_type').contains('structural'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('fire alarm'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('paint'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('public toilet'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('bike rack'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('non-residential heat'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('scaffold'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('electric'), 'Building Infrastructure')
                                                     .when(col('complaint_type').contains('parking'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('parking meter'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('derelict'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('driveway'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('abandoned vehicle'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('panhandeling'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('food vendor'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('Streetlight'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('sidewalk'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('sidewalk'), 'Parking and Street')
                                                     .when(col('complaint_type').contains('drug'), 'Health')
                                                     .when(col('complaint_type').contains('hazard'), 'Health')
                                                     .when(col('complaint_type').contains('unsanitary'), 'Health')
                                                     .when(col('complaint_type').contains('sanitation'), 'Health')
                                                     .when(col('complaint_type').contains('mosquitos'), 'Health')
                                                     .when(col('complaint_type').contains('asbestos'), 'Health')
                                                     .when(col('complaint_type').contains('mold'), 'Health')
                                                     .when(col('complaint_type').contains('sewer'), 'Health')
                                                     .when(col('complaint_type').contains('air quality'), 'Health')
                                                     .when(col('complaint_type').contains('lead'), 'Health')
                                                     .when(col('complaint_type').contains('health'), 'Health')
                                                     .when(col('complaint_type').contains('covid'), 'Health')
                                                     .when(col('complaint_type').contains('gas'), 'Health')
                                                     .when(col('complaint_type').contains('industrial waste'), 'Health')
                                                     .when(col('complaint_type').contains('food poisoning'), 'Health')
                                                     .when(col('complaint_type').contains('radioactive'), 'Health')
                                                     .when(col('complaint_type').contains('bees'), 'Health')
                                                     .when(col('complaint_type').contains('dirty'), 'Health')
                                                     .when(col('complaint_type').contains('urinating'), 'Health')
                                                     .when(col('complaint_type').contains('animal'), 'Animal')
                                                     .when(col('complaint_type').contains('trapping pigeon'), 'Animal')
                                                     .when(col('complaint_type').contains('unlicensed dog'), 'Animal')
                                                     .when(col('complaint_type').contains('pet'), 'Animal')
                                                     .when(col('complaint_type').contains('pet'), 'Animal')
                                                     .otherwise('Other'))
complaints_replaced.show(1000)



# Count unique values
# df_selected.count()
# unique_counts = df_selected.select(countDistinct('id'))
# unique_counts.show()
# df_selected.groupBy('id').count().show()
# df_selected.groupBy(['latitude', 'longitude']).count().show()
# df_selected.show()
# df_selected.printSchema()

spark.stop()
# Append to the table
 # df.write.jdbc(url, table="abb", mode="append", properties=props)
