sudo wget -O calendar_40.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-07-05/data/calendar.csv.gz"
gunzip calendar_40.csv.gz
aws s3 cp calendar_40.csv s3://edenbucket
rm calendar_40.csv
sudo wget -O calendar_41.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-08-06/data/calendar.csv.gz"
gunzip calendar_41.csv.gz
aws s3 cp calendar_41.csv s3://edenbucket
rm calendar_41.csv
sudo wget -O calendar_42.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-09-08/data/calendar.csv.gz"
gunzip calendar_42.csv.gz
aws s3 cp calendar_42.csv s3://edenbucket
rm calendar_42.csv
sudo wget -O calendar_43.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-10-03/data/calendar.csv.gz"
gunzip calendar_43.csv.gz
aws s3 cp calendar_43.csv s3://edenbucket
rm calendar_43.csv
sudo wget -O calendar_44.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-11-03/data/calendar.csv.gz"
gunzip calendar_44.csv.gz
aws s3 cp calendar_44.csv s3://edenbucket
rm calendar_44.csv
sudo wget -O calendar_45.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2018-12-06/data/calendar.csv.gz"
gunzip calendar_45.csv.gz
aws s3 cp calendar_45.csv s3://edenbucket
rm calendar_45.csv
sudo wget -O calendar_46.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-01-09/data/calendar.csv.gz"
gunzip calendar_46.csv.gz
aws s3 cp calendar_46.csv s3://edenbucket
rm calendar_46.csv
sudo wget -O calendar_47.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-02-01/data/calendar.csv.gz"
gunzip calendar_47.csv.gz
aws s3 cp calendar_47.csv s3://edenbucket
rm calendar_47.csv
sudo wget -O calendar_48.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-03-06/data/calendar.csv.gz"
gunzip calendar_48.csv.gz
aws s3 cp calendar_48.csv s3://edenbucket
rm calendar_48.csv
sudo wget -O calendar_49.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-04-03/data/calendar.csv.gz"
gunzip calendar_49.csv.gz
aws s3 cp calendar_49.csv s3://edenbucket
rm calendar_49.csv
