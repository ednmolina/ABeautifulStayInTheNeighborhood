sudo wget -O calendar_50.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-05-03/data/calendar.csv.gz"
gunzip calendar_50.csv.gz
aws s3 cp calendar_50.csv s3://edenbucket
rm calendar_50.csv
sudo wget -O calendar_51.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-06-02/data/calendar.csv.gz"
gunzip calendar_51.csv.gz
aws s3 cp calendar_51.csv s3://edenbucket
rm calendar_51.csv
sudo wget -O calendar_52.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-07-08/data/calendar.csv.gz"
gunzip calendar_52.csv.gz
aws s3 cp calendar_52.csv s3://edenbucket
rm calendar_52.csv
sudo wget -O calendar_53.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-08-06/data/calendar.csv.gz"
gunzip calendar_53.csv.gz
aws s3 cp calendar_53.csv s3://edenbucket
rm calendar_53.csv
sudo wget -O calendar_54.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/data/calendar.csv.gz"
gunzip calendar_54.csv.gz
aws s3 cp calendar_54.csv s3://edenbucket
rm calendar_54.csv
sudo wget -O calendar_55.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-10-14/data/calendar.csv.gz"
gunzip calendar_55.csv.gz
aws s3 cp calendar_55.csv s3://edenbucket
rm calendar_55.csv
sudo wget -O calendar_56.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-11-01/data/calendar.csv.gz"
gunzip calendar_56.csv.gz
aws s3 cp calendar_56.csv s3://edenbucket
rm calendar_56.csv
sudo wget -O calendar_57.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-12-04/data/calendar.csv.gz"
gunzip calendar_57.csv.gz
aws s3 cp calendar_57.csv s3://edenbucket
rm calendar_57.csv
sudo wget -O calendar_58.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-01-03/data/calendar.csv.gz"
gunzip calendar_58.csv.gz
aws s3 cp calendar_58.csv s3://edenbucket
rm calendar_58.csv
sudo wget -O calendar_59.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2020-02-12/data/calendar.csv.gz"
gunzip calendar_59.csv.gz
aws s3 cp calendar_59.csv s3://edenbucket
rm calendar_59.csv
