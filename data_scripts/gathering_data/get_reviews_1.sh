sudo wget -O review_0.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-01-01/data/reviews.csv.gz"
gunzip review_0.csv.gz
aws s3 cp review_0.csv s3://edenbucket
rm review_0.csv
sudo wget -O review_1.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-03-01/data/reviews.csv.gz"
gunzip review_1.csv.gz
aws s3 cp review_1.csv s3://edenbucket
rm review_1.csv
sudo wget -O review_2.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-05-01/data/reviews.csv.gz"
gunzip review_2.csv.gz
aws s3 cp review_2.csv s3://edenbucket
rm review_2.csv
sudo wget -O review_3.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-06-01/data/reviews.csv.gz"
gunzip review_3.csv.gz
aws s3 cp review_3.csv s3://edenbucket
rm review_3.csv
sudo wget -O review_4.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-08-01/data/reviews.csv.gz"
gunzip review_4.csv.gz
aws s3 cp review_4.csv s3://edenbucket
rm review_4.csv
sudo wget -O review_5.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-09-01/data/reviews.csv.gz"
gunzip review_5.csv.gz
aws s3 cp review_5.csv s3://edenbucket
rm review_5.csv
sudo wget -O review_6.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-10-01/data/reviews.csv.gz"
gunzip review_6.csv.gz
aws s3 cp review_6.csv s3://edenbucket
rm review_6.csv
sudo wget -O review_7.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-11-01/data/reviews.csv.gz"
gunzip review_7.csv.gz
aws s3 cp review_7.csv s3://edenbucket
rm review_7.csv
sudo wget -O review_8.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-11-20/data/reviews.csv.gz"
gunzip review_8.csv.gz
aws s3 cp review_8.csv s3://edenbucket
rm review_8.csv
sudo wget -O review_9.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-12-02/data/reviews.csv.gz"
gunzip review_9.csv.gz
aws s3 cp review_9.csv s3://edenbucket
rm review_9.csv
