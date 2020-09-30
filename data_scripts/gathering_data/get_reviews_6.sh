sudo wget -O review_50.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-05-03/data/reviews.csv.gz"
gunzip review_50.csv.gz
aws s3 cp review_50.csv s3://edenbucket
rm review_50.csv
sudo wget -O review_51.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-06-02/data/reviews.csv.gz"
gunzip review_51.csv.gz
aws s3 cp review_51.csv s3://edenbucket
rm review_51.csv
sudo wget -O review_52.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-07-08/data/reviews.csv.gz"
gunzip review_52.csv.gz
aws s3 cp review_52.csv s3://edenbucket
rm review_52.csv
sudo wget -O review_53.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-08-06/data/reviews.csv.gz"
gunzip review_53.csv.gz
aws s3 cp review_53.csv s3://edenbucket
rm review_53.csv
sudo wget -O review_54.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/data/reviews.csv.gz"
gunzip review_54.csv.gz
aws s3 cp review_54.csv s3://edenbucket
rm review_54.csv
sudo wget -O review_55.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-10-14/data/reviews.csv.gz"
gunzip review_55.csv.gz
aws s3 cp review_55.csv s3://edenbucket
rm review_55.csv
sudo wget -O review_56.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-11-01/data/reviews.csv.gz"
gunzip review_56.csv.gz
aws s3 cp review_56.csv s3://edenbucket
rm review_56.csv
sudo wget -O review_57.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-12-04/data/reviews.csv.gz"
gunzip review_57.csv.gz
aws s3 cp review_57.csv s3://edenbucket
rm review_57.csv
sudo wget -O review_58.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-01-03/data/reviews.csv.gz"
gunzip review_58.csv.gz
aws s3 cp review_58.csv s3://edenbucket
rm review_58.csv
sudo wget -O review_59.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-02-12/data/reviews.csv.gz"
gunzip review_59.csv.gz
aws s3 cp review_59.csv s3://edenbucket
rm review_59.csv
