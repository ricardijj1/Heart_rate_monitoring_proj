## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

These missing values can be from a misread data from the heart monitor. The missing data can be do to environmental factors. Filtering these out help us get a better reading of our data. The risk factor from doing that, is that key data are missed and changes in heart rate can appear most drastic. The other risk factor is that whatever we can learn from the "no signal" values is not being considered. 

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

The standard deviation graph is the graph with the less trend becasue standard deviation in the context of heart rate describe the average amount of time the heart rate is different from the average.

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

When looking at the averages graph most of the values are in the close together at the center of the graph. But there are drastic differences along the x-axis at the start and at the end. 

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

The arevages graph follows a trend while the stdevs graph is more scattered. The other different between the graphs is the the average graph is easier to read and understandable.
