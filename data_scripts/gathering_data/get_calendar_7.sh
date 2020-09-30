sudo wget -O calendar_60.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-03-13/data/calendar.csv.gz"
gunzip calendar_60.csv.gz
aws s3 cp calendar_60.csv s3://edenbucket
rm calendar_60.csv
sudo wget -O calendar_61.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-04-08/data/calendar.csv.gz"
gunzip calendar_61.csv.gz
aws s3 cp calendar_61.csv s3://edenbucket
rm calendar_61.csv
sudo wget -O calendar_62.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-05-06/data/calendar.csv.gz"
gunzip calendar_62.csv.gz
aws s3 cp calendar_62.csv s3://edenbucket
rm calendar_62.csv
sudo wget -O calendar_63.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-06-08/data/calendar.csv.gz"
gunzip calendar_63.csv.gz
aws s3 cp calendar_63.csv s3://edenbucket
rm calendar_63.csv
sudo wget -O calendar_64.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-07-07/data/calendar.csv.gz"
gunzip calendar_64.csv.gz
aws s3 cp calendar_64.csv s3://edenbucket
rm calendar_64.csv
sudo wget -O calendar_65.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-08-15/data/calendar.csv.gz"
gunzip calendar_65.csv.gz
aws s3 cp calendar_65.csv s3://edenbucket
rm calendar_65.csv
