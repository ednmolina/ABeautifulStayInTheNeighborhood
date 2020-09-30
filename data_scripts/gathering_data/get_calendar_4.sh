sudo wget -O calendar_30.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-10-02/data/calendar.csv.gz"
gunzip calendar_30.csv.gz
aws s3 cp calendar_30.csv s3://edenbucket
rm calendar_30.csv
sudo wget -O calendar_31.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-11-01/data/calendar.csv.gz"
gunzip calendar_31.csv.gz
aws s3 cp calendar_31.csv s3://edenbucket
rm calendar_31.csv
sudo wget -O calendar_32.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2017-12-02/data/calendar.csv.gz"
gunzip calendar_32.csv.gz
aws s3 cp calendar_32.csv s3://edenbucket
rm calendar_32.csv
sudo wget -O calendar_33.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-01-10/data/calendar.csv.gz"
gunzip calendar_33.csv.gz
aws s3 cp calendar_33.csv s3://edenbucket
rm calendar_33.csv
sudo wget -O calendar_34.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-01-10/data/calendar.csv.gz"
gunzip calendar_34.csv.gz
aws s3 cp calendar_34.csv s3://edenbucket
rm calendar_34.csv
sudo wget -O calendar_35.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-02-02/data/calendar.csv.gz"
gunzip calendar_35.csv.gz
aws s3 cp calendar_35.csv s3://edenbucket
rm calendar_35.csv
sudo wget -O calendar_36.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-03-04/data/calendar.csv.gz"
gunzip calendar_36.csv.gz
aws s3 cp calendar_36.csv s3://edenbucket
rm calendar_36.csv
sudo wget -O calendar_37.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-04-06/data/calendar.csv.gz"
gunzip calendar_37.csv.gz
aws s3 cp calendar_37.csv s3://edenbucket
rm calendar_37.csv
sudo wget -O calendar_38.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-05-09/data/calendar.csv.gz"
gunzip calendar_38.csv.gz
aws s3 cp calendar_38.csv s3://edenbucket
rm calendar_38.csv
sudo wget -O calendar_39.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-06-03/data/calendar.csv.gz"
gunzip calendar_39.csv.gz
aws s3 cp calendar_39.csv s3://edenbucket
rm calendar_39.csv
