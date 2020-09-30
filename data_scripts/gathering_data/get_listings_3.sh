sudo wget -O listing_20.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-12-03/data/listings.csv.gz"
gunzip listing_20.csv.gz
aws s3 cp listing_20.csv s3://edenbucket
rm listing_20.csv
sudo wget -O listing_21.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-01-01/data/listings.csv.gz"
gunzip listing_21.csv.gz
aws s3 cp listing_21.csv s3://edenbucket
rm listing_21.csv
sudo wget -O listing_22.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-02-02/data/listings.csv.gz"
gunzip listing_22.csv.gz
aws s3 cp listing_22.csv s3://edenbucket
rm listing_22.csv
sudo wget -O listing_23.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-03-02/data/listings.csv.gz"
gunzip listing_23.csv.gz
aws s3 cp listing_23.csv s3://edenbucket
rm listing_23.csv
sudo wget -O listing_24.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-04-02/data/listings.csv.gz"
gunzip listing_24.csv.gz
aws s3 cp listing_24.csv s3://edenbucket
rm listing_24.csv
sudo wget -O listing_25.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-05-02/data/listings.csv.gz"
gunzip listing_25.csv.gz
aws s3 cp listing_25.csv s3://edenbucket
rm listing_25.csv
sudo wget -O listing_26.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-06-02/data/listings.csv.gz"
gunzip listing_26.csv.gz
aws s3 cp listing_26.csv s3://edenbucket
rm listing_26.csv
sudo wget -O listing_27.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-07-02/data/listings.csv.gz"
gunzip listing_27.csv.gz
aws s3 cp listing_27.csv s3://edenbucket
rm listing_27.csv
sudo wget -O listing_28.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-08-02/data/listings.csv.gz"
gunzip listing_28.csv.gz
aws s3 cp listing_28.csv s3://edenbucket
rm listing_28.csv
sudo wget -O listing_29.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-09-02/data/listings.csv.gz"
gunzip listing_29.csv.gz
aws s3 cp listing_29.csv s3://edenbucket
rm listing_29.csv
