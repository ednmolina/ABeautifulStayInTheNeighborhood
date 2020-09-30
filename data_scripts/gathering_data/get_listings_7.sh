sudo wget -O listing_60.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-03-13/data/listings.csv.gz"
gunzip listing_60.csv.gz
aws s3 cp listing_60.csv s3://edenbucket
rm listing_60.csv
sudo wget -O listing_61.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-04-08/data/listings.csv.gz"
gunzip listing_61.csv.gz
aws s3 cp listing_61.csv s3://edenbucket
rm listing_61.csv
sudo wget -O listing_62.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-05-06/data/listings.csv.gz"
gunzip listing_62.csv.gz
aws s3 cp listing_62.csv s3://edenbucket
rm listing_62.csv
sudo wget -O listing_63.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-06-08/data/listings.csv.gz"
gunzip listing_63.csv.gz
aws s3 cp listing_63.csv s3://edenbucket
rm listing_63.csv
sudo wget -O listing_64.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-07-07/data/listings.csv.gz"
gunzip listing_64.csv.gz
aws s3 cp listing_64.csv s3://edenbucket
rm listing_64.csv
sudo wget -O listing_65.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-08-15/data/listings.csv.gz"
gunzip listing_65.csv.gz
aws s3 cp listing_65.csv s3://edenbucket
rm listing_65.csv
