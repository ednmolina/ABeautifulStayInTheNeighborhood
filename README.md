# Be Our Guest
When booking a place to stay users typically know what part of town they want to stay. Choosing the right Airbnb can come down to a few key features not yet captured in the Airbnb listing such as neighborhood activity (like noise in the area) and price fluctuation over the past 30 days. Be Our Guest enables users to view common 311 complaints. A visualization of the Airbnb listings, nearest complaints, and other information can be seen on [this site](http://datapipe.space/).

## Website
![alt text](https://github.com/ednmolina/ABeautifulStayInTheNeighborhood/blob/master/images/SiteSC.png)
On the site, a user can choose several filters to distill the information they wish to see. For example a user can filter by location, complaint, time, as well as price. A user can also hover over a listing on the map to view the canonical information about the listing such as the number of bedrooms, bathrooms, price, as well as the enriched information as determined by the 311 data set which includes the top 311 complaint within a 100 m radius of that listing for the current month, when complaints are reported for the current month, as well as the average price of the listing for the current month. A listing can also be clicked on and the url to the listing will be displayed.

## Slides
Slides for this project can be found [here](https://drive.google.com/file/d/1-TQZkxUxceVeY-Pso_QqxdlZ0znTqofb/view?usp=sharing).

## Datasets
The two datasets used in this projects come from Airbnb and NYC Open Data. There are five years of listing, review, and pricing data available from Airbnb. The [NYC Airbnb](http://insideairbnb.com/get-the-data.html) totals to around 60+ GB. The [311 complaints dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) contains complaints from 2010 to the present. This data amounts to around 13 GB.

For this project the data was gathered early September 2020 so only listing information up until August 2020 can be used. This is because Airbnb releases listing, review, and pricing data at the end of each month.
