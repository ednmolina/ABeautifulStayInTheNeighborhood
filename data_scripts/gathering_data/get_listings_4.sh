sudo wget -O listing_30.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-10-02/data/listings.csv.gz"
gunzip listing_30.csv.gz
aws s3 cp listing_30.csv s3://edenbucket
rm listing_30.csv
sudo wget -O listing_31.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-11-01/data/listings.csv.gz"
gunzip listing_31.csv.gz
aws s3 cp listing_31.csv s3://edenbucket
rm listing_31.csv
sudo wget -O listing_32.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-12-02/data/listings.csv.gz"
gunzip listing_32.csv.gz
aws s3 cp listing_32.csv s3://edenbucket
rm listing_32.csv
sudo wget -O listing_33.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-01-10/data/listings.csv.gz"
gunzip listing_33.csv.gz
aws s3 cp listing_33.csv s3://edenbucket
rm listing_33.csv
sudo wget -O listing_34.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-01-10/data/listings.csv.gz"
gunzip listing_34.csv.gz
aws s3 cp listing_34.csv s3://edenbucket
rm listing_34.csv
sudo wget -O listing_35.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-02-02/data/listings.csv.gz"
gunzip listing_35.csv.gz
aws s3 cp listing_35.csv s3://edenbucket
rm listing_35.csv
sudo wget -O listing_36.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-03-04/data/listings.csv.gz"
gunzip listing_36.csv.gz
aws s3 cp listing_36.csv s3://edenbucket
rm listing_36.csv
sudo wget -O listing_37.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-04-06/data/listings.csv.gz"
gunzip listing_37.csv.gz
aws s3 cp listing_37.csv s3://edenbucket
rm listing_37.csv
sudo wget -O listing_38.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-05-09/data/listings.csv.gz"
gunzip listing_38.csv.gz
aws s3 cp listing_38.csv s3://edenbucket
rm listing_38.csv
sudo wget -O listing_39.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-06-03/data/listings.csv.gz"
gunzip listing_39.csv.gz
aws s3 cp listing_39.csv s3://edenbucket
rm listing_39.csv
