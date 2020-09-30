sudo wget -O review_60.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-03-13/data/reviews.csv.gz"
gunzip review_60.csv.gz
aws s3 cp review_60.csv s3://edenbucket
rm review_60.csv
sudo wget -O review_61.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-04-08/data/reviews.csv.gz"
gunzip review_61.csv.gz
aws s3 cp review_61.csv s3://edenbucket
rm review_61.csv
sudo wget -O review_62.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-05-06/data/reviews.csv.gz"
gunzip review_62.csv.gz
aws s3 cp review_62.csv s3://edenbucket
rm review_62.csv
sudo wget -O review_63.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-06-08/data/reviews.csv.gz"
gunzip review_63.csv.gz
aws s3 cp review_63.csv s3://edenbucket
rm review_63.csv
sudo wget -O review_64.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-07-07/data/reviews.csv.gz"
gunzip review_64.csv.gz
aws s3 cp review_64.csv s3://edenbucket
rm review_64.csv
sudo wget -O review_65.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-08-15/data/reviews.csv.gz"
gunzip review_65.csv.gz
aws s3 cp review_65.csv s3://edenbucket
rm review_65.csv
