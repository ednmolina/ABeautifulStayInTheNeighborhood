sudo wget -O listing_0.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-01-01/data/listings.csv.gz"
gunzip listing_0.csv.gz
aws s3 cp listing_0.csv s3://edenbucket
rm listing_0.csv
sudo wget -O listing_1.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-03-01/data/listings.csv.gz"
gunzip listing_1.csv.gz
aws s3 cp listing_1.csv s3://edenbucket
rm listing_1.csv
sudo wget -O listing_2.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-05-01/data/listings.csv.gz"
gunzip listing_2.csv.gz
aws s3 cp listing_2.csv s3://edenbucket
rm listing_2.csv
sudo wget -O listing_3.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-06-01/data/listings.csv.gz"
gunzip listing_3.csv.gz
aws s3 cp listing_3.csv s3://edenbucket
rm listing_3.csv
sudo wget -O listing_4.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-08-01/data/listings.csv.gz"
gunzip listing_4.csv.gz
aws s3 cp listing_4.csv s3://edenbucket
rm listing_4.csv
sudo wget -O listing_5.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-09-01/data/listings.csv.gz"
gunzip listing_5.csv.gz
aws s3 cp listing_5.csv s3://edenbucket
rm listing_5.csv
sudo wget -O listing_6.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-10-01/data/listings.csv.gz"
gunzip listing_6.csv.gz
aws s3 cp listing_6.csv s3://edenbucket
rm listing_6.csv
sudo wget -O listing_7.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-11-01/data/listings.csv.gz"
gunzip listing_7.csv.gz
aws s3 cp listing_7.csv s3://edenbucket
rm listing_7.csv
sudo wget -O listing_8.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-11-20/data/listings.csv.gz"
gunzip listing_8.csv.gz
aws s3 cp listing_8.csv s3://edenbucket
rm listing_8.csv
sudo wget -O listing_9.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-12-02/data/listings.csv.gz"
gunzip listing_9.csv.gz
aws s3 cp listing_9.csv s3://edenbucket
rm listing_9.csv
