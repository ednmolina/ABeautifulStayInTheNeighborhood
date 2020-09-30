sudo wget -O calendar_10.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-01-01/data/calendar.csv.gz"
gunzip calendar_10.csv.gz
aws s3 cp calendar_10.csv s3://edenbucket
rm calendar_10.csv
sudo wget -O calendar_11.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-02-02/data/calendar.csv.gz"
gunzip calendar_11.csv.gz
aws s3 cp calendar_11.csv s3://edenbucket
rm calendar_11.csv
sudo wget -O calendar_12.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-04-03/data/calendar.csv.gz"
gunzip calendar_12.csv.gz
aws s3 cp calendar_12.csv s3://edenbucket
rm calendar_12.csv
sudo wget -O calendar_13.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-05-02/data/calendar.csv.gz"
gunzip calendar_13.csv.gz
aws s3 cp calendar_13.csv s3://edenbucket
rm calendar_13.csv
sudo wget -O calendar_14.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-06-02/data/calendar.csv.gz"
gunzip calendar_14.csv.gz
aws s3 cp calendar_14.csv s3://edenbucket
rm calendar_14.csv
sudo wget -O calendar_15.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-07-02/data/calendar.csv.gz"
gunzip calendar_15.csv.gz
aws s3 cp calendar_15.csv s3://edenbucket
rm calendar_15.csv
sudo wget -O calendar_16.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-08-02/data/calendar.csv.gz"
gunzip calendar_16.csv.gz
aws s3 cp calendar_16.csv s3://edenbucket
rm calendar_16.csv
sudo wget -O calendar_17.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-09-02/data/calendar.csv.gz"
gunzip calendar_17.csv.gz
aws s3 cp calendar_17.csv s3://edenbucket
rm calendar_17.csv
sudo wget -O calendar_18.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-10-01/data/calendar.csv.gz"
gunzip calendar_18.csv.gz
aws s3 cp calendar_18.csv s3://edenbucket
rm calendar_18.csv
sudo wget -O calendar_19.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2016-11-02/data/calendar.csv.gz"
gunzip calendar_19.csv.gz
aws s3 cp calendar_19.csv s3://edenbucket
rm calendar_19.csv
