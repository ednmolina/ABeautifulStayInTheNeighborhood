sudo wget -O listing_40.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-07-05/data/listings.csv.gz"
gunzip listing_40.csv.gz
aws s3 cp listing_40.csv s3://edenbucket
rm listing_40.csv
sudo wget -O listing_41.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-08-06/data/listings.csv.gz"
gunzip listing_41.csv.gz
aws s3 cp listing_41.csv s3://edenbucket
rm listing_41.csv
sudo wget -O listing_42.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-09-08/data/listings.csv.gz"
gunzip listing_42.csv.gz
aws s3 cp listing_42.csv s3://edenbucket
rm listing_42.csv
sudo wget -O listing_43.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-10-03/data/listings.csv.gz"
gunzip listing_43.csv.gz
aws s3 cp listing_43.csv s3://edenbucket
rm listing_43.csv
sudo wget -O listing_44.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-11-03/data/listings.csv.gz"
gunzip listing_44.csv.gz
aws s3 cp listing_44.csv s3://edenbucket
rm listing_44.csv
sudo wget -O listing_45.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-12-06/data/listings.csv.gz"
gunzip listing_45.csv.gz
aws s3 cp listing_45.csv s3://edenbucket
rm listing_45.csv
sudo wget -O listing_46.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-01-09/data/listings.csv.gz"
gunzip listing_46.csv.gz
aws s3 cp listing_46.csv s3://edenbucket
rm listing_46.csv
sudo wget -O listing_47.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-02-01/data/listings.csv.gz"
gunzip listing_47.csv.gz
aws s3 cp listing_47.csv s3://edenbucket
rm listing_47.csv
sudo wget -O listing_48.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-03-06/data/listings.csv.gz"
gunzip listing_48.csv.gz
aws s3 cp listing_48.csv s3://edenbucket
rm listing_48.csv
sudo wget -O listing_49.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-04-03/data/listings.csv.gz"
gunzip listing_49.csv.gz
aws s3 cp listing_49.csv s3://edenbucket
rm listing_49.csv
