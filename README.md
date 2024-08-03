# Airline On-Time Performance
### Longitudinal Trends, Carrier Delays, and Geographic Patterns in the US Airline Industry

![pandas](https://img.shields.io/badge/Pandas-white?logo=pandas&logoColor=black)
![numpy](https://img.shields.io/badge/NumPy-white?logo=Numpy&logoColor=grey)
![plotly](https://img.shields.io/badge/plotly-white?logo=plotly)
![matplotlib](https://img.shields.io/badge/matplotlib-white?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxODAiIGhlaWdodD0iMTgwIiBzdHJva2U9ImdyYXkiPgo8ZyBzdHJva2Utd2lkdGg9IjIiIGZpbGw9IiNGRkYiPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSI4OCIvPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSI2NiIvPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSI0NCIvPgo8Y2lyY2xlIGN4PSI5MCIgY3k9IjkwIiByPSIyMiIvPgo8cGF0aCBkPSJtOTAsMnYxNzZtNjItMjYtMTI0LTEyNG0xMjQsMC0xMjQsMTI0bTE1MC02MkgyIi8%2BCjwvZz48ZyBvcGFjaXR5PSIuOCI%2BCjxwYXRoIGZpbGw9IiM0NEMiIGQ9Im05MCw5MGgxOGExOCwxOCAwIDAsMCAwLTV6Ii8%2BCjxwYXRoIGZpbGw9IiNCQzMiIGQ9Im05MCw5MCAzNC00M2E1NSw1NSAwIDAsMC0xNS04eiIvPgo8cGF0aCBmaWxsPSIjRDkzIiBkPSJtOTAsOTAtMTYtNzJhNzQsNzQgMCAwLDAtMzEsMTV6Ii8%2BCjxwYXRoIGZpbGw9IiNEQjMiIGQ9Im05MCw5MC01OC0yOGE2NSw2NSAwIDAsMC01LDM5eiIvPgo8cGF0aCBmaWxsPSIjM0JCIiBkPSJtOTAsOTAtMzMsMTZhMzcsMzcgMCAwLDAgMiw1eiIvPgo8cGF0aCBmaWxsPSIjM0M5IiBkPSJtOTAsOTAtMTAsNDVhNDYsNDYgMCAwLDAgMTgsMHoiLz4KPHBhdGggZmlsbD0iI0Q3MyIgZD0ibTkwLDkwIDQ2LDU4YTc0LDc0IDAgMCwwIDEyLTEyeiIvPgo8L2c%2BPC9zdmc%2B)
![seaborn](https://img.shields.io/badge/seaborn-white?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI%2FPgo8IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDIwMDEwOTA0Ly9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9UUi8yMDAxL1JFQy1TVkctMjAwMTA5MDQvRFREL3N2ZzEwLmR0ZCI%2BCjxzdmcgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiB3aWR0aD0iMTg1MC4wMDAwMDBwdCIgaGVpZ2h0PSIxODUwLjAwMDAwMHB0IiB2aWV3Qm94PSIwIDAgMTg1MC4wMDAwMDAgMTg1MC4wMDAwMDAiCiBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCBtZWV0Ij4KCjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuMDAwMDAwLDE4NTAuMDAwMDAwKSBzY2FsZSgwLjEwMDAwMCwtMC4xMDAwMDApIgpmaWxsPSIjMDAwMDAwIiBzdHJva2U9Im5vbmUiPgo8cGF0aCBkPSJNODgzOSAxODQ4OSBjLTIxMDMgLTk1IC00MDk2IC04OTggLTU2OTIgLTIyOTEgLTIxMCAtMTg0IC02NjUgLTYzOQotODQ2IC04NDYgLTg2OCAtOTk3IC0xNTAyIC0yMTI5IC0xODg2IC0zMzcyIC0zODkgLTEyNjAgLTUwNSAtMjU4MyAtMzM5Ci0zOTAwIDIxOCAtMTc0MiA5NDAgLTM0MDUgMjA2MyAtNDc1NCA1NjkgLTY4NCAxMjIyIC0xMjczIDE5NTYgLTE3NjYgMTIwMwotODA2IDI1NzIgLTEzMTkgNDAwNSAtMTUwMCA0MTYgLTUyIDQ3OSAtNTUgMTE1NSAtNTUgNjg4IDAgNzQwIDMgMTE5NCA2MQoxNTY5IDIwMSAzMDg4IDgxNyA0MzUxIDE3NjYgMzg1IDI4OSA2NjIgNTI5IDEwMDUgODczIDEwMTUgMTAxNiAxNzY1IDIyMjUKMjIyMCAzNTgwIDI0MCA3MTMgMzcyIDEzNDAgNDUyIDIxNDAgMTUgMTUzIDE4IDI3NyAxOCA4MjAgMCA2NzYgLTMgNzM5IC01NQoxMTU1IC0yOTQgMjMyOSAtMTQ2MCA0NDU4IC0zMjY2IDU5NjEgLTE3NjQgMTQ2OSAtNDAzOCAyMjMzIC02MzM1IDIxMjh6IG05MzEKLTMxOSBjODI2IC01MiAxNjA5IC0yMDYgMjM3MCAtNDY1IDI0MTIgLTgyMyA0MzU2IC0yNjM0IDUzNTEgLTQ5ODMgNTY1IC0xMzMzCjc5OCAtMjgwNCA2NzQgLTQyMzkgLTE0NSAtMTY2OCAtNzUxIC0zMjU2IC0xNzUwIC00NTkyIC0yNzEgLTM2MSAtNTA3IC02MzQKLTg0MCAtOTY2IC0zMzIgLTMzMyAtNjA1IC01NjkgLTk2NiAtODQwIC0xODc5IC0xNDA2IC00MjUyIC0yMDIwIC02NTY0IC0xNjk5Ci0yNzY2IDM4NCAtNTE4MyAyMDIwIC02NTYxIDQ0NDIgLTY3NSAxMTg4IC0xMDY5IDI1MTkgLTExNTQgMzkwMiAtMTMgMjE0IC0xMwo4MDMgMCAxMDIzIDEyMyAyMDU5IDk0NSA0MDA5IDIzMjcgNTUxOSAxNDIgMTU1IDQ3MSA0ODIgNjIzIDYxOSA4OTQgODA4IDE5OTIKMTQ0NiAzMTU1IDE4MzQgNzI5IDI0MyAxNTA2IDM5NCAyMjgwIDQ0NCAxOTEgMTIgODY0IDEzIDEwNTUgMXoiLz4KPHBhdGggZD0iTTY3NTAgMTAxMTMgYy0xMDIwIC0yNCAtMjA4OCAtMjcyIC0zMzYyIC03ODIgLTQ1OCAtMTgzIC04NDkgLTM1MwotMTc0MyAtNzU4IC0zNTcgLTE2MyAtNzMxIC0zMzEgLTgzMCAtMzc1IC05OSAtNDQgLTE4MSAtODEgLTE4MiAtODIgLTMgLTMgMzEKLTIzMCA1OCAtMzgxIDEzNSAtNzgxIDM5NCAtMTU3OCA3NDYgLTIzMDAgbDU4IC0xMjAgMyA0ODggMiA0ODcgMTAwNSAwIDEwMDUKMCAwIDY5NSAwIDY5NSAxMDAwIDAgMTAwMCAwIDAgMTI1IDAgMTI1IDEwNzUgMCAxMDc1IDAgMCAtNTYwIDAgLTU2MCAxMDAwIDAKMTAwMCAwIDAgLTc3MCAwIC03NzAgMTAwNSAwIDEwMDUgMCAwIC01MzAgMCAtNTMwIDEwMDAgMCAxMDAwIDAgMCAtMjI1IDAKLTIyNSAxMDAwIDAgMTAwMCAwIDAgLTE5NyAxIC0xOTggMzIgMzYgYzE4IDIwIDg0IDk3IDE0OCAxNzAgNjI5IDcyOCAxMTM1CjE1NjcgMTQ5NCAyNDc0IDEwMSAyNTcgMjE4IDU5NCAyMTEgNjEyIC0zIDcgLTEzIDEzIC0yMSAxMyAtNTIgMCAtNzk0IDE3NwotMTEzMSAyNzAgLTY2OCAxODQgLTEzNzYgNDI1IC0yMTEwIDcxOCAtNTQ3IDIxOCAtOTY3IDQwMSAtMTk5NCA4NjcgLTEzMzMKNjA1IC0xOTEzIDg0OCAtMjUzNSAxMDYyIC0xMDk5IDM4MCAtMjA3MCA1NDkgLTMwMTUgNTI2eiIvPgo8cGF0aCBkPSJNNTY1OCA0NTU4IGwtMyAtMzIzMyA4NCAtMzggYzQ4NCAtMjE3IDExMjQgLTQyNSAxNjU5IC01NDEgbDExMiAtMjQKMCAzNTM0IDAgMzUzNCAtOTI1IDAgLTkyNSAwIC0yIC0zMjMyeiIvPgo8cGF0aCBkPSJNMzY1MCA1MDY1IGwwIC0yNDc0IDExMyAtOTIgYzQ2NCAtMzgxIDEwNTUgLTc2MyAxNjE2IC0xMDQ0IGwxMzEKLTY1IDAgMzA3NSAwIDMwNzUgLTkzMCAwIC05MzAgMCAwIC0yNDc1eiIvPgo8cGF0aCBkPSJNNzY2MCAzNjgxIGwwIC0yOTg5IDY2IC0xMSBjMjYzIC00NiA1NzQgLTg2IDg2OSAtMTExIDcyIC03IDMwOSAtMTQKNTI4IC0xNyBsMzk3IC02IDAgMzA2MiAwIDMwNjEgLTkzMCAwIC05MzAgMCAwIC0yOTg5eiIvPgo8cGF0aCBkPSJNMTY0OCA1NTg4IGwtMyAtNTUzIDI5IC01NSBjNjEgLTExMiAyMTMgLTM2MSAzMzEgLTU0MCAzNjcgLTU1NiA4MjIKLTEwOTUgMTI5NSAtMTUzNiAxMDAgLTkzIDE4OCAtMTczIDE5NiAtMTc3IDEyIC03IDE0IDIyOSAxNCAxNzAzIGwwIDE3MTAKLTkzMCAwIC05MzAgMCAtMiAtNTUyeiIvPgo8cGF0aCBkPSJNOTY2MCAyODQwIGwwIC0yMjgwIDY4IDAgYzk0IDAgMzgxIDI2IDYxOCA1NSAzNDQgNDMgNjQ0IDk5IDk4NyAxODIKbDE4NyA0NiAwIDIxMzggMCAyMTM5IC05MzAgMCAtOTMwIDAgMCAtMjI4MHoiLz4KPHBhdGggZD0iTTExNjcwIDI0NzUgYzAgLTg3MiA0IC0xNTg1IDggLTE1ODUgNDEgMCA1NzIgMTgyIDgxNyAyODAgMjkxIDExNgo3MzAgMzI0IDk1NSA0NTIgbDc1IDQzIC0zIDExOTggLTIgMTE5NyAtOTI1IDAgLTkyNSAwIDAgLTE1ODV6Ii8%2BCjxwYXRoIGQ9Ik0xMzY3MCAyNjg0IGwwIC05MzYgNDggMjggYzUyOSAzMDcgMTEzNCA3NzMgMTYyNCAxMjUzIGwxODggMTgzIDAKMjA0IDAgMjA0IC05MzAgMCAtOTMwIDAgMCAtOTM2eiIvPgo8L2c%2BCjwvc3ZnPgo%3D)


The project explores on-time performance trends from 34 years of US domestic flight data, focusing on variations across carriers, routes, airports, and time. The exploratory data analysis (EDA) resulted in a comprehensive report with 35+ data insights and 25+ visualizations, converted into an interactive Streamlit dashboard. The analysis demonstrates how to extract critical performance trends from historical data, enabling stakeholders to make informed decisions and significantly boost operational efficiency in the aviation industry.

📌 **WRITE-UP**: [Project Write-Up](https://marcocamilo.com/portfolio/airline-performance)  
🐍 **NOTEBOOK**: [Jupyter Notebook](https://github.com/marcocamilo/airline-on-time/tree/main/src)  

## 🚀 Key Takeaways

1. **Stagnation in On-Time Performance**: Despite a slight decrease in delay volatility, the analysis reveals that arrival delays have only decreased by 1% over 34 years, while departure delays have increased by 5%. This highlights a persistent challenge in improving overall on-time performance.
2. **Limitations in Delay Optimization**: Arrival delays can be minimized by up to 45 minutes relative to departure delays, but can also exceed them by up to 250 minutes. This highlights significant variability in delay patterns and emphasizes the need for targeted strategies to manage both types of delays effectively.
3. **Top Delayed Carriers**: JetBlue Airways, ExpressJet Airlines, and Frontier Airlines consistently rank among the top carriers with the highest frequency of delays, both at departure and arrival.
4. **Airports with Highest Delay Counts**: The top three airports with the highest total delay counts are Chicago O'Hare International Airport, Hartsfield-Jackson Atlanta International Airport, and Dallas/Fort Worth International Airport.

[👇 Jump to results and discussion](#-results-and-discussion)

## 📋 Motivation

I chose this project to tackle a large longitudinal dataset and deepen my understanding of the aviation industry, a field of personal interest. My goal was to apply rigorous statistical and data exploration techniques to provide more precise and insightful answers to key industry questions than typical media reports. This project also offered an ideal opportunity to refine my skills in exploratory data analysis, preparing me to effectively address real-world challenges using big data.

## 🎯 Approach

1. **Data Collection**: The [Airline Reporting Carrier On-Time Performance Dataset](https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FGJ) was obtained from the [IBM Developer](https://developer.ibm.com/exchanges/data/all/airline/) website, covering detailed records of 2 million flights over 34 years.
2. **Data Preprocessing**: The preprocessing strategy integrated univariate analysis with data cleaning and feature engineering, focusing on three main areas: analyzing distribution and spread, refining flight information variables, and adjusting time variables.
3. **Univariate Analysis**: Each variable was examined for its distribution, spread, and missing values to identify patterns and trends, which informed subsequent preprocessing and analysis.
4. **Bivariate Analysis**: Relationships between variables were investigated in relation to the research questions.
5. **Visualization**: Findings were visualized using an interactive dashboard created with Streamlit.

## 🔨 Preprocessing

The preprocessing strategy aimed to ensure the data was clean, consistent, and ready for analysis through a combination of univariate analysis, data cleaning, and feature engineering. This process focused on three key areas:

1. **Exploring Spread and Distribution**: We analyzed the spread and distribution of each variable to identify patterns and trends that would guide subsequent preprocessing steps.
2. **Preprocessing Flight Info Variables**: The initial phase of preprocessing concentrated on flight information variables, including date, flight details, origin/destination, and departure/arrival data.
3. **(Re)Engineering Time Variables**: The second phase addressed challenges in handling time variables, particularly the calculation of delays from raw timestamps. This involved:
   - **Imputing Time Zone Information**: Correcting time zone discrepancies.
   - **Reverse Engineering Arrival Dates**: Accurately determining arrival dates.
   - **Filtering Remaining Negative Delays**: Removing erroneous negative delay values.
   - **Recalculating Departure and Arrival Delays**: Adjusting delay calculations to account for time zone differences, cross-midnight flights, and daylight savings time.

## 🚀 Exploratory Data Analysis

The exploratory data analysis (EDA) focused on addressing four key industry questions from a longitudinal perspective, examining historical trends over 34 years. The analysis was organized around four main themes, with each question answered through relevant visualizations of the variables of interest:

### Longitudinal Analysis: How do delays vary across time?

![](./output/img/evolution-mean-delays.png)

### Correlation Analysis: How are departures delays correlated with arrival delays?

<div class="grid">
    <div class="g-col-6 g-col-md-12">
        <img src="./output/img/delays-correlation.png" alt="Correlation between Departure and Arrival Delays">
    </div>
    <div class="g-col-6 g-col-md-12">
        <img src="./output/img/delays-correlation-filtered-bounds.png" alt="Correlation between Departure and Arrival Delays (Filtered)">
    </div>
</div>

### Corporate Analysis: How do delays vary across carriers?

![](./output/img/carrier-delays.png)

### Geographical Analysis: How do delays vary by airport?

![](./output/img/arr-delay-airports.png)

## 📈 Results and Discussion

### Longitudinal Analysis

The longitudinal analysis focused on understanding how delays varied across time, with the following key findings:

- **Narrowing Gap in Delays**: The evolution of delays over 34 years shows a narrowing gap between departure and arrival delays, driven by a 5% increase in departure delays rather than a decrease in arrival delays.
- **Stabilization in Volatility**: The volatility of delays has slightly decreased over the years, suggesting stabilization in seasonal delay patterns.
- **Small Decrease in Arrival Delays**: Arrival delays have decreased by only 1% over 34 years, while departure delays have increased by over 5%, indicating stagnation in improving on-time performance.

### Correlation Analysis

The correlation analysis aimed to understand the relationship between departure and arrival delays, with the following key findings:

- **Strong Positive Relationship**: Departure and arrival delays exhibit a strong positive linear relationship, with a Pearson correlation coefficient of 0.93.
- **Dispersion in Relationship**: Within the interquartile range, the correlation coefficient drops to 0.67, indicating variability in the relationship between departure and arrival delays.
- **Bounds of Delay Dispersion**: Arrival delays can be minimized by up to 45 minutes relative to departure delays, yet can exceed them by up to 250 minutes, reflecting different causes influencing each type of delay.
- **Different Causes for Delays**: Departure delays are more within the carrier's control, while arrival delays are influenced by external factors such as weather and airport congestion.
  
### Corporate Analysis

The corporate analysis aimed to understand how delays varied across carriers, with the following key findings:

- **Top Delayed Carriers**: JetBlue Airways, ExpressJet Airlines, and Frontier Airlines consistently rank among the top carriers with the highest frequency of delays, both at departure and arrival.
- **Largest Difference**: Southwest Airlines shows the largest difference between departure and arrival delays, ranking 5th in departure delays but 20th in arrival delays.
- **Indicator of Carrier Control**: Departure delays are more indicative of carrier performance, influenced by factors like boarding, fueling, and maintenance.

### Geographical Analysis

The geographical analysis aimed to understand how delays varied by airport, with the following key findings:

- **Highest Delay Counts**: The top five airports with the highest total delay counts are Chicago O'Hare International Airport, Hartsfield-Jackson Atlanta International Airport, Dallas/Fort Worth International Airport, Los Angeles International Airport, and San Francisco International Airport.
- **Coastal Congestion**: Coastal airports like Los Angeles, San Francisco, Newark, and Boston rank high among the top 15 airports, indicating congestion and operational difficulties in these regions.
- **Nationwide Issue**: The geographical spread of the top 20 airports shows that delays are widespread across the country, highlighting a nationwide issue rather than a localized problem.

## 🪐 Future Work

1. **Explore Impact of Weather**: Incorporate weather data to understand the impact of weather conditions on flight delays and identify the most common weather-related causes of delays.
2. **Longitudinal Analysis**: conduct a time series analysis to explore the evolution of these variables over time and identify any seasonal patterns or trends.
3. **Predictive Modeling**: Develop a predictive model to forecast delays based on historical data, using machine learning algorithms such as XGBoost Regressor, Random Forest Regressor, or LSTM Neural Networks.

## 📚 References

- [Airline Reporting Carrier On-Time Performance Dataset](https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FGJ)
- [IBM Developer Data Source](https://developer.ibm.com/exchanges/data/all/airline/)
- [Streamlit Documentation](https://docs.streamlit.io/)
