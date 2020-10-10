sudo wget -O listing_50.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-05-03/data/listings.csv.gz"
gunzip listing_50.csv.gz
aws s3 cp listing_50.csv s3://edenbucket
rm listing_50.csv
sudo wget -O listing_51.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-06-02/data/listings.csv.gz"
gunzip listing_51.csv.gz
aws s3 cp listing_51.csv s3://edenbucket
rm listing_51.csv
sudo wget -O listing_52.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-07-08/data/listings.csv.gz"
gunzip listing_52.csv.gz
aws s3 cp listing_52.csv s3://edenbucket
rm listing_52.csv
sudo wget -O listing_53.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-08-06/data/listings.csv.gz"
gunzip listing_53.csv.gz
aws s3 cp listing_53.csv s3://edenbucket
rm listing_53.csv
sudo wget -O listing_54.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/data/listings.csv.gz"
gunzip listing_54.csv.gz
aws s3 cp listing_54.csv s3://edenbucket
rm listing_54.csv
sudo wget -O listing_55.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-10-14/data/listings.csv.gz"
gunzip listing_55.csv.gz
aws s3 cp listing_55.csv s3://edenbucket
rm listing_55.csv
sudo wget -O listing_56.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-11-01/data/listings.csv.gz"
gunzip listing_56.csv.gz
aws s3 cp listing_56.csv s3://edenbucket
rm listing_56.csv
sudo wget -O listing_57.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-12-04/data/listings.csv.gz"
gunzip listing_57.csv.gz
aws s3 cp listing_57.csv s3://edenbucket
rm listing_57.csv
sudo wget -O listing_58.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-01-03/data/listings.csv.gz"
gunzip listing_58.csv.gz
aws s3 cp listing_58.csv s3://edenbucket
rm listing_58.csv
sudo wget -O listing_59.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-02-12/data/listings.csv.gz"
gunzip listing_59.csv.gz
aws s3 cp listing_59.csv s3://edenbucket
rm listing_59.csv
