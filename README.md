# Surfs Up

## Overview

  For this project, I used SQLite to test code on weather data from Oahu, Hawaii, taken over a 7-year time period. In order to perform this analysis, SQLAlchemy was also used to help me query only the data that I needed from the weather database. SQLAlchemy is a query tool designed for SQLite and the integration of statistical analysis and dataframe analysis. A primary feature of this tool is the ORM, or Object Relational Mapper. ORM allows one to create classes in their code, that can be used to map to specific tables in a given database. This ability is helpful for those who want to perform data analysis on a decoupled system.

  SQLite is a version of SQL that does not have users, and lives on a computer or phone, and has been used to help create various applications, for example, Itunes and Photoshop. All SQLite databases are flat files, meaning they don't have relationships that connect the data to anything else, and this is the reason that these files can be stored locally, which also provides the benefit of being able to perform quick analysis'. A local database is preferable for those who want to setup a database engine to test and make sure their code works, as opposed to having to set up a SQL database server. The steps needed to set up an entire SQL database server is not always super convenient when one just wants to test something out. 

## Purpose 

  I was considering opening a Surf and Shake Shop in Oahu, Hawaii, but in order to fulfill this dream, I knew I would need some investors. One potential investor showed interest, but before he would decide to put pen to paper, he wanted more information and a provided analysis on Oahu's weather data, which has been stored in an SQLite database. This is why SQLAlchemy was a necessary tool for this analysis, because it allowed me to easily connect to the SQLite database. Thus, allowing me to query the weather data using specific parameters, for example, my investor wanted to see temperature data for the months of June and December. The weather data consisted of gathered precipitation and temperature observation measurements taken by multiple stations, for the dates ranging from Jan 1, 2010 to Aug 23, 2017. In order to determine if the the surf and ice cream shop business is sustainable year-round, the temperature data for the months of June and December was analyzed. 

## Resources

* Python 3.9.12
* Anaconda 4.13.0 (Jupyter Notebook, Visual Studio Code)
* SQLite 
* SQLAlchemy 
* MatPlotLib, NumPy, Pandas, Datetime
* Weather Data: hawaii.sqlite

## The Data 

  In order to connect to the SQLite database engine, I had to create an 'engine' variable and set it equal to the 'create_engine()' function, and include the location of my SQLite database file, 'hawaii.sqlite', as my parameter inside that function. Once connected, I could then access the data inside that database, and perform queries on it. The 'automap_base()' function was used to reflect the database into a new model, or essentially transferring the database contents into a different structure of data. It does this by creating a base class for an automap schema in SQLAlchemy. 

  Now, that the environment for SQLAlchemy was set up, I used the 'prepare()' function to reflect the database tables. Reflecting these tables was necessary, so that I could create classes within the whole dataset, and these classes are what allows me to keep my code separated. By keeping the code separated, if there were other classes or systems that wanted to interact with it, then those classes or systems will be able to interact with only specific subsets of data, as opposed to the whole dataset. As shown below (Fig. A), is an example of how the engine was created and how the two functions, 'automap_base()' and 'prepare()', were used. 

Fig. A) 

![Fig_A](https://user-images.githubusercontent.com/104864579/184411850-c56e89c6-964d-4838-bb9c-7c92fbc445a4.png)

  Then, I used another function, 'Base.classes.keys()', in order to reference the classes that were mapped in each table, in which the output showed that 'measurement' and 'station' were the two classes, or tables, that could be referenced. By knowing the proper class names, I could then reference each specific class using the 'Base.classes' method, and give the classes new variable names, 'Measurement' and 'Station'. I created these new variables, so that I could use those variables every time I wanted to reference the measurement or station classes without having to type out 'Base.classes.<class name>' over and over again, (Fig. B). 

Fig. B)

![Fig_B](https://user-images.githubusercontent.com/104864579/184411898-61b15095-8e87-4fa8-b935-e6ed0a7e33ce.png)

  In order to use Python to query the weather data, I had to use an SQLAlchemy session link to the database. I did this by setting: 'session = Session(engine)'.  Using 'session.query()' function, I was able to reference the 'Measurement' table, and specific columns within that table. Because I only needed to retrieve the temperatures for a specific month, I decided to reference the columns, 'date' and 'tobs'. 

  Then, I created a 'sel' list, that included the referenced columns from the measurement class/table. I created a variable to set my session.query() function equal to, and then filtered the month of interest into my query. I had to use a statistical function, 'func.strftime()', so that I could filter out only the dates from the measurement class, that were equal to the month of interest. As shown below, I have provided examples of how I was able to write a query to filter the Measurement table to retrieve the temperatures for the month of June,(Fig. C), and the month of December, (Fig. D). 

Fig. C) 

![Fig_C](https://user-images.githubusercontent.com/104864579/184411931-9c09327a-4331-470b-84e3-b709c86b9cf5.png)

Fig. D) 

![Fig_D](https://user-images.githubusercontent.com/104864579/184411949-8d301d22-6712-4cd2-ba74-bc994bacc456.png)

  Following both queries, I converted the output, for my June and December temperatures, into a list. By doing this, I was then able to use Pandas to create a DataFrame, one dataframe for my June temperatures list(Fig. E), and a second dataframe for my December temperatures list(Fig. F). 

Fig. E) 

![Fig_E](https://user-images.githubusercontent.com/104864579/184412005-10b6d90e-7a92-4df9-b322-44ccc31798f5.png)

Fig. F) 

![Fig_F](https://user-images.githubusercontent.com/104864579/184412035-d5c69d90-c30a-4156-b45b-cc7dc73f52ba.png)

  Using the newly created dataframes, I used the '.describe()' function to print out the summary statistics of the temperatures for both months: June and December.   


## Results 

  The two images, provided below (Fig. G & Fig. H) depict the summary statistics that resulted from my Oahu weather data analysis, using the '.describe()' method. 

Fig. G: June Summary Statistics)

![Fig_G](https://user-images.githubusercontent.com/104864579/184412074-c754d7fa-6954-4da8-9b3e-5cc5da11a020.png)

Fig. H: December Summary Statistics)

![Fig_H](https://user-images.githubusercontent.com/104864579/184412108-82f62887-e8a5-42c0-8ed1-67eb0625c9f2.png)

  By looking at the summary statistics for the months of June and December, in which the data was collected over a 7-year period, a couple of differences can be seen: 

  * The measurement count for the month of June came out to 1700, while December only contained 1517 measurement counts, which is a difference of 183. This is most likely due to the fact that the weather database only had measurements taken from Jan 1, 2010, until Aug 23, 2017. If the database contained data measurements up to the end of 2017, it is likely that the December temperature measurement count would have been higher. 

  * The minimum temperature for the month of June was 64.0 degrees, while the minimum temperature for the month of December was 56 degrees, which is a difference of 9 degrees between the two months. The minimum temperature statistic tells the lowest temperature that was seen ever over the course of the 7-year time period. 

  * The mean temperature for the month of June was 74.94 degrees, and the mean temperature for the month of December was 71.04 degrees, which is only a difference of 3 degrees, roughly. 

  * The quartile ranges for the month of June is between 73.0 degrees (for the 25% quartile) and 77.0 degress (for the 75% quartile), while the quartile ranges for the month of December is between 69.0 degrees (for the 25% quartile) and 74.0 degrees (for the 75% quartile). This shows that the ranges in degrees for the month of June is smaller, than the range in degrees for the month of December, which is larger. 

## Summary

  The minimum temperatures for the two months analyzed only differentiated by 9 degrees, which is kind of surprising, because most would assume that the June min temperature would be higher because it is summer time, while December would be expected to be cold. The reason that this is not a good statistic to base the probable temperature of both months on, is because this statistic just tells you whats the lowest temperature ever recorded over the 7 year period that the measurement data was collected. These temperatures would probably be considered outliers within the data because one year may have been abnormally cold compared to the rest of the years. 

  Comparing the mean temperatures for both months, the mean temperature only differs by 3 degrees or so, which could mean that the temperature on Oahu stays relatively the same throughout the year, and the expectation that summer months would be hotter, while winter months would be colder, doesn't really apply on Oahu. 

  Although, the temperatures might not differ too much, it doesn't provide any information about how often it rained on Oahu. Considering, it would make more sense to surf when it isn't raining, it would be a good idea to include the precipitation data for the months of June and December. Including the precipitation data along with temperature data, could provide more insight as to what kind of weather you would expect to have. Thus, if it rains a lot in December, then you wouldn't expect as many sales for a surf and ice cream shop. 

  Another thing to consider for this analysis, is to take counts of how many measurements were recorded per year for the months of June and December, as well as, filtering out the data to analyze temperature observations for the past couple years vs. the past 7 years. Instead of just looking at the summary statistics, I think a better way to look at data taken over the course of 7 years, would be to look at a trend line to see how the weather changes from year to year. 

 I would also consider the count of how many measurements each station was taken. If one station was recording the majority of the weather data, then the data would be slightly skewed to report the temperature observations in the area around that stations lat/long. 

  It might also be a good idea to see how far apart these stations are from one another, and to make sure to only include the weather data from the stations that are closest to areas that more tourists or surfers would visit, because the more tourists/surfers, the higher the expected sales.




