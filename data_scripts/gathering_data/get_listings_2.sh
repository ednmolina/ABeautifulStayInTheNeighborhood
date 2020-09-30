sudo wget -O listing_10.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-01-01/data/listings.csv.gz"
gunzip listing_10.csv.gz
aws s3 cp listing_10.csv s3://edenbucket
rm listing_10.csv
sudo wget -O listing_11.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-02-02/data/listings.csv.gz"
gunzip listing_11.csv.gz
aws s3 cp listing_11.csv s3://edenbucket
rm listing_11.csv
sudo wget -O listing_12.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-04-03/data/listings.csv.gz"
gunzip listing_12.csv.gz
aws s3 cp listing_12.csv s3://edenbucket
rm listing_12.csv
sudo wget -O listing_13.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-05-02/data/listings.csv.gz"
gunzip listing_13.csv.gz
aws s3 cp listing_13.csv s3://edenbucket
rm listing_13.csv
sudo wget -O listing_14.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-06-02/data/listings.csv.gz"
gunzip listing_14.csv.gz
aws s3 cp listing_14.csv s3://edenbucket
rm listing_14.csv
sudo wget -O listing_15.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-07-02/data/listings.csv.gz"
gunzip listing_15.csv.gz
aws s3 cp listing_15.csv s3://edenbucket
rm listing_15.csv
sudo wget -O listing_16.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-08-02/data/listings.csv.gz"
gunzip listing_16.csv.gz
aws s3 cp listing_16.csv s3://edenbucket
rm listing_16.csv
sudo wget -O listing_17.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-09-02/data/listings.csv.gz"
gunzip listing_17.csv.gz
aws s3 cp listing_17.csv s3://edenbucket
rm listing_17.csv
sudo wget -O listing_18.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-10-01/data/listings.csv.gz"
gunzip listing_18.csv.gz
aws s3 cp listing_18.csv s3://edenbucket
rm listing_18.csv
sudo wget -O listing_19.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-11-02/data/listings.csv.gz"
gunzip listing_19.csv.gz
aws s3 cp listing_19.csv s3://edenbucket
rm listing_19.csv
