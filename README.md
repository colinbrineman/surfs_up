# surfs_up

## Purpose

The purpose of this analysis is to determine whether a particular location in Hawaii is suitable for opening a combined ice cream parlor/surfing supplies shop. Understandably, it is important to the individual who wishes to start this shop that the weather at the location be suitable for year-round revenue. Thus, the basis of this analysis is a comparison of the prospective location's temperature statistics at different times of the year, namely, summer (June) & winter (December).

## Results

### Summary statistics
||June|December|
|---|---|---|
|count|1700|1517|
|mean|74.944118|71.041529|
|std|3.257417|3.74592|
|min|64|56|
|0.25|73|69|
|0.5|75|71|
|0.75|77|74|
|max|85|83|

### Findings
A major part of Hawaii's success as a tourist location is its remarkably temperate weather — & the results of my query of weather data for the location reflect that.

Some conclusions one could draw from the above are that:
1. **The site has almost the same average temperatures in June as in December.** The difference between average temperatures in June vs. December is less than 4℉. By comparison, where I live in Baltimore, Maryland, the difference between average temperatures in June vs. December is approximately 36℉ (see: [Weather Spark](https://weatherspark.com/y/21918/Average-Weather-in-Baltimore-Maryland-United-States-Year-Round)).
2. **The site is slightly colder in December vs. June.** On every single metric measuring temperature — mean, minimum, 25th percentile, median, 75th percentile, & maximum — the site is colder in December than it is in January.
3. **Temperature at the site is slightly more variable in December than in June.** The standard deviation of temperature observations in June is about 3.25℉, whereas the standard deviation for December is about 3.75℉.

## Additional investigations recommended
I would recommend the following additional queries to be made of the data available for the site:
1. **Precipitation data needs to be taken into account.** Regardless of the temperature, people are going to stay inside when it is rainy. This means they are less likely to go out for an ice cream or a surf. Precipitation data is available & should be given the same weight as temperature data when determining whether to invest in a business on the site.
2. **Additional months' temperatures should be analyzed as well.** Given that Hawaii is a tropical location, northerly latitudes' conceptions of "winter" & "summer" likely have little relevance to Hawaiian weather. One could conclude from the June & December data that Hawaii is the perfect temperature year-round. But to make this assumption without analyzing the other 10 months' worth of data seems unnecessarily speculative, given that the data is readily available.