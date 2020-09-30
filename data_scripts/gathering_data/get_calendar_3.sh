sudo wget -O calendar_20.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-12-03/data/calendar.csv.gz"
gunzip calendar_20.csv.gz
aws s3 cp calendar_20.csv s3://edenbucket
rm calendar_20.csv
sudo wget -O calendar_21.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-01-01/data/calendar.csv.gz"
gunzip calendar_21.csv.gz
aws s3 cp calendar_21.csv s3://edenbucket
rm calendar_21.csv
sudo wget -O calendar_22.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-02-02/data/calendar.csv.gz"
gunzip calendar_22.csv.gz
aws s3 cp calendar_22.csv s3://edenbucket
rm calendar_22.csv
sudo wget -O calendar_23.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-03-02/data/calendar.csv.gz"
gunzip calendar_23.csv.gz
aws s3 cp calendar_23.csv s3://edenbucket
rm calendar_23.csv
sudo wget -O calendar_24.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-04-02/data/calendar.csv.gz"
gunzip calendar_24.csv.gz
aws s3 cp calendar_24.csv s3://edenbucket
rm calendar_24.csv
sudo wget -O calendar_25.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-05-02/data/calendar.csv.gz"
gunzip calendar_25.csv.gz
aws s3 cp calendar_25.csv s3://edenbucket
rm calendar_25.csv
sudo wget -O calendar_26.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-06-02/data/calendar.csv.gz"
gunzip calendar_26.csv.gz
aws s3 cp calendar_26.csv s3://edenbucket
rm calendar_26.csv
sudo wget -O calendar_27.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-07-02/data/calendar.csv.gz"
gunzip calendar_27.csv.gz
aws s3 cp calendar_27.csv s3://edenbucket
rm calendar_27.csv
sudo wget -O calendar_28.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-08-02/data/calendar.csv.gz"
gunzip calendar_28.csv.gz
aws s3 cp calendar_28.csv s3://edenbucket
rm calendar_28.csv
sudo wget -O calendar_29.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-09-02/data/calendar.csv.gz"
gunzip calendar_29.csv.gz
aws s3 cp calendar_29.csv s3://edenbucket
rm calendar_29.csv
