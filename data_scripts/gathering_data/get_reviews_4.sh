sudo wget -O review_30.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-10-02/data/reviews.csv.gz"
gunzip review_30.csv.gz
aws s3 cp review_30.csv s3://edenbucket
rm review_30.csv
sudo wget -O review_31.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-11-01/data/reviews.csv.gz"
gunzip review_31.csv.gz
aws s3 cp review_31.csv s3://edenbucket
rm review_31.csv
sudo wget -O review_32.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-12-02/data/reviews.csv.gz"
gunzip review_32.csv.gz
aws s3 cp review_32.csv s3://edenbucket
rm review_32.csv
sudo wget -O review_33.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-01-10/data/reviews.csv.gz"
gunzip review_33.csv.gz
aws s3 cp review_33.csv s3://edenbucket
rm review_33.csv
sudo wget -O review_34.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-01-10/data/reviews.csv.gz"
gunzip review_34.csv.gz
aws s3 cp review_34.csv s3://edenbucket
rm review_34.csv
sudo wget -O review_35.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-02-02/data/reviews.csv.gz"
gunzip review_35.csv.gz
aws s3 cp review_35.csv s3://edenbucket
rm review_35.csv
sudo wget -O review_36.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-03-04/data/reviews.csv.gz"
gunzip review_36.csv.gz
aws s3 cp review_36.csv s3://edenbucket
rm review_36.csv
sudo wget -O review_37.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-04-06/data/reviews.csv.gz"
gunzip review_37.csv.gz
aws s3 cp review_37.csv s3://edenbucket
rm review_37.csv
sudo wget -O review_38.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-05-09/data/reviews.csv.gz"
gunzip review_38.csv.gz
aws s3 cp review_38.csv s3://edenbucket
rm review_38.csv
sudo wget -O review_39.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-06-03/data/reviews.csv.gz"
gunzip review_39.csv.gz
aws s3 cp review_39.csv s3://edenbucket
rm review_39.csv
