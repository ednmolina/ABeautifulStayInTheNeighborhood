from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
import json

# Load the configuration s3file
with open("config.json") as config_json:
    config = json.load(config_json)
    
# Data Config
region = 'us-west-1'
bucket = config['s3']['bucket']
# Update to iterate over the 65 listings csv's; append to postgre
key = 'listing_1.csv'

sc = SparkContext()
sc._jsc.hadoopConfiguration().set('fs.s3a.endpoint', f's3-{region}.amazonaws.com')

spark = SparkSession(sc)

# Postgres Config
mode = "append"
#mode = "overwrite"
url = f"jdbc:postgresql://{config['postgre']['ip']}:{config['postgre']['port']}/{config['postgre']['db']}"
properties = {"user": config['postgre']['user'],
              "password": config['postgre']['password'],
              "driver": "org.postgresql.Driver"}

# Read Data from S3
s3file = f's3a://{bucket}/{key}'
raw_df = spark.read.csv(s3file, header = True, inferSchema=True, multiLine=True, escape='"')

columns = ['id', 'latitude', 'longitude', 'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'jurisdiction_names', 'number_of_reviews', 'price', 'street', 'bathrooms', 'bedrooms']
# , 'price','neighbourhood_cleansed', 'neighborhood_group_cleansed','price', 'bathrooms_text', 'bedrooms', 'minimum_nights'
 # [minimum_nights, review_scores_rating, last_scraped, host_id, bed_type, calendar_last_scraped, host_since, maximum_nights, availability_365, space,
 # requires_license, neighbourhood_cleansed, review_scores_value, review_scores_communication, review_scores_accuracy, availability_90, state, neighbourhood_group_cleansed,
 # jurisdiction_names, id, neighbourhood, last_review, calculated_host_listings_count, host_location, summary, host_response_time, listing_url, host_response_rate, availability_60,
 # review_scores_location, monthly_price, square_feet, host_url, bathrooms, reviews_per_month, host_picture_url, host_about, review_scores_cleanliness, number_of_reviews, license, country, scrape_id, review_scores_checkin, price, street, beds, latitude,
 # picture_url, description, availability_30, property_type, first_review, guests_included, market, host_acceptance_rate, longitude, weekly_price, calendar_updated, zipcode, host_name, room_type, extra_people, city, accommodates,
 # is_location_exact, host_is_superhost, name, bedrooms]
df_selected = raw_df.select(columns)
df_selected.show() # it works!

# Count unique values
df_selected.count()
unique_counts = df_selected.select(countDistinct('id'))
unique_counts.show()
# df_selected.groupBy('id').count().show()
# df_selected.groupBy(['latitude', 'longitude']).count().show()
df_selected.printSchema()

spark.stop()
# Append to the table
 # df.write.jdbc(url=url, table = 'test_table', properties=properties, mode = 'append')
