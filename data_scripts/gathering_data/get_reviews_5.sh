sudo wget -O review_40.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-07-05/data/reviews.csv.gz"
gunzip review_40.csv.gz
aws s3 cp review_40.csv s3://edenbucket
rm review_40.csv
sudo wget -O review_41.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-08-06/data/reviews.csv.gz"
gunzip review_41.csv.gz
aws s3 cp review_41.csv s3://edenbucket
rm review_41.csv
sudo wget -O review_42.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-09-08/data/reviews.csv.gz"
gunzip review_42.csv.gz
aws s3 cp review_42.csv s3://edenbucket
rm review_42.csv
sudo wget -O review_43.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-10-03/data/reviews.csv.gz"
gunzip review_43.csv.gz
aws s3 cp review_43.csv s3://edenbucket
rm review_43.csv
sudo wget -O review_44.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-11-03/data/reviews.csv.gz"
gunzip review_44.csv.gz
aws s3 cp review_44.csv s3://edenbucket
rm review_44.csv
sudo wget -O review_45.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-12-06/data/reviews.csv.gz"
gunzip review_45.csv.gz
aws s3 cp review_45.csv s3://edenbucket
rm review_45.csv
sudo wget -O review_46.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-01-09/data/reviews.csv.gz"
gunzip review_46.csv.gz
aws s3 cp review_46.csv s3://edenbucket
rm review_46.csv
sudo wget -O review_47.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-02-01/data/reviews.csv.gz"
gunzip review_47.csv.gz
aws s3 cp review_47.csv s3://edenbucket
rm review_47.csv
sudo wget -O review_48.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-03-06/data/reviews.csv.gz"
gunzip review_48.csv.gz
aws s3 cp review_48.csv s3://edenbucket
rm review_48.csv
sudo wget -O review_49.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-04-03/data/reviews.csv.gz"
gunzip review_49.csv.gz
aws s3 cp review_49.csv s3://edenbucket
rm review_49.csv
