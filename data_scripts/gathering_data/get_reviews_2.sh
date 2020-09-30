sudo wget -O review_10.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-01-01/data/reviews.csv.gz"
gunzip review_10.csv.gz
aws s3 cp review_10.csv s3://edenbucket
rm review_10.csv
sudo wget -O review_11.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-02-02/data/reviews.csv.gz"
gunzip review_11.csv.gz
aws s3 cp review_11.csv s3://edenbucket
rm review_11.csv
sudo wget -O review_12.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-04-03/data/reviews.csv.gz"
gunzip review_12.csv.gz
aws s3 cp review_12.csv s3://edenbucket
rm review_12.csv
sudo wget -O review_13.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-05-02/data/reviews.csv.gz"
gunzip review_13.csv.gz
aws s3 cp review_13.csv s3://edenbucket
rm review_13.csv
sudo wget -O review_14.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-06-02/data/reviews.csv.gz"
gunzip review_14.csv.gz
aws s3 cp review_14.csv s3://edenbucket
rm review_14.csv
sudo wget -O review_15.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-07-02/data/reviews.csv.gz"
gunzip review_15.csv.gz
aws s3 cp review_15.csv s3://edenbucket
rm review_15.csv
sudo wget -O review_16.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-08-02/data/reviews.csv.gz"
gunzip review_16.csv.gz
aws s3 cp review_16.csv s3://edenbucket
rm review_16.csv
sudo wget -O review_17.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-09-02/data/reviews.csv.gz"
gunzip review_17.csv.gz
aws s3 cp review_17.csv s3://edenbucket
rm review_17.csv
sudo wget -O review_18.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-10-01/data/reviews.csv.gz"
gunzip review_18.csv.gz
aws s3 cp review_18.csv s3://edenbucket
rm review_18.csv
sudo wget -O review_19.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-11-02/data/reviews.csv.gz"
gunzip review_19.csv.gz
aws s3 cp review_19.csv s3://edenbucket
rm review_19.csv
