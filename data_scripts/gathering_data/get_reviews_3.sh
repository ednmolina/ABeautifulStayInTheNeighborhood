sudo wget -O review_20.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-12-03/data/reviews.csv.gz"
gunzip review_20.csv.gz
aws s3 cp review_20.csv s3://edenbucket
rm review_20.csv
sudo wget -O review_21.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-01-01/data/reviews.csv.gz"
gunzip review_21.csv.gz
aws s3 cp review_21.csv s3://edenbucket
rm review_21.csv
sudo wget -O review_22.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-02-02/data/reviews.csv.gz"
gunzip review_22.csv.gz
aws s3 cp review_22.csv s3://edenbucket
rm review_22.csv
sudo wget -O review_23.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-03-02/data/reviews.csv.gz"
gunzip review_23.csv.gz
aws s3 cp review_23.csv s3://edenbucket
rm review_23.csv
sudo wget -O review_24.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-04-02/data/reviews.csv.gz"
gunzip review_24.csv.gz
aws s3 cp review_24.csv s3://edenbucket
rm review_24.csv
sudo wget -O review_25.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-05-02/data/reviews.csv.gz"
gunzip review_25.csv.gz
aws s3 cp review_25.csv s3://edenbucket
rm review_25.csv
sudo wget -O review_26.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-06-02/data/reviews.csv.gz"
gunzip review_26.csv.gz
aws s3 cp review_26.csv s3://edenbucket
rm review_26.csv
sudo wget -O review_27.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-07-02/data/reviews.csv.gz"
gunzip review_27.csv.gz
aws s3 cp review_27.csv s3://edenbucket
rm review_27.csv
sudo wget -O review_28.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-08-02/data/reviews.csv.gz"
gunzip review_28.csv.gz
aws s3 cp review_28.csv s3://edenbucket
rm review_28.csv
sudo wget -O review_29.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-09-02/data/reviews.csv.gz"
gunzip review_29.csv.gz
aws s3 cp review_29.csv s3://edenbucket
rm review_29.csv
