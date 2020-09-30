sudo wget -O calendar_0.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-01-01/data/calendar.csv.gz"
gunzip calendar_0.csv.gz
aws s3 cp calendar_0.csv s3://edenbucket
rm calendar_0.csv
sudo wget -O calendar_1.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-03-01/data/calendar.csv.gz"
gunzip calendar_1.csv.gz
aws s3 cp calendar_1.csv s3://edenbucket
rm calendar_1.csv
sudo wget -O calendar_2.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-05-01/data/calendar.csv.gz"
gunzip calendar_2.csv.gz
aws s3 cp calendar_2.csv s3://edenbucket
rm calendar_2.csv
sudo wget -O calendar_3.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-06-01/data/calendar.csv.gz"
gunzip calendar_3.csv.gz
aws s3 cp calendar_3.csv s3://edenbucket
rm calendar_3.csv
sudo wget -O calendar_4.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-08-01/data/calendar.csv.gz"
gunzip calendar_4.csv.gz
aws s3 cp calendar_4.csv s3://edenbucket
rm calendar_4.csv
sudo wget -O calendar_5.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-09-01/data/calendar.csv.gz"
gunzip calendar_5.csv.gz
aws s3 cp calendar_5.csv s3://edenbucket
rm calendar_5.csv
sudo wget -O calendar_6.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-10-01/data/calendar.csv.gz"
gunzip calendar_6.csv.gz
aws s3 cp calendar_6.csv s3://edenbucket
rm calendar_6.csv
sudo wget -O calendar_7.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-11-01/data/calendar.csv.gz"
gunzip calendar_7.csv.gz
aws s3 cp calendar_7.csv s3://edenbucket
rm calendar_7.csv
sudo wget -O calendar_8.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-11-20/data/calendar.csv.gz"
gunzip calendar_8.csv.gz
aws s3 cp calendar_8.csv s3://edenbucket
rm calendar_8.csv
# sudo wget -O calendar_9.csv.gz "http://data.insideairbnb.com/united-states/ny/new-york-city/2015-12-02/data/calendar.csv.gz"
