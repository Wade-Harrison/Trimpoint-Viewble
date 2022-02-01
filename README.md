Answers to Questions:
2) Consider the data set below. Write some python code that illustrates
some common feature engineering and/or data preparation tasks.

https://raw.githubusercontent.com/mathcoder3141/blog-data-files/master/Congre
ss_White_House.csv

https://github.com/helloworlddata/white-house-salaries/blob/master/data/converte
d/2017.csv

Consider the file “data.csv” in the following GitHub repository. What
are some descriptive statistics about this set? What can you say about the
distribution of this data?
https://github.com/fractalbass/data_engineer

No code is necessary for the following questions:
3) If you were asked to impute null values in a column of a file that was
365 Gigabytes, what would you do? What tools would you use?
What tools would you NOT use?
\N
ANSWER3:
  _to input null values in an entire column of a large file. I would use either python or sql. to do this in python I would use the datascience library to create a new table using the column header and then a zero array that is set to the length of the table and then join the new table and the old one. In sequal I would use the UPDATE TABLE_NAME SET [COLUMN_NAME] = NULL SCRIPT. The tool that I would not use would be a loop in python as that would take a very long time to iterate over each line just to add a NULL values. I also would stray away from excel even though this would be easiest it is above the maximum size file that excel can handle. \N
  _
4) What would you do if you were asked to do the above task every
Thursday morning at 2:00am?
  To complete the previous task at thursday at 2 am I would use SQL server, then by adding a new job I can schedule a command to run at a scheduled time at different intervals       daily/weekly etc. 

5) Who is your favorite mathematician, statistician or computer scientist
and why?
  My favorite mathmatician is Carl Gauss simply put I beleive that his work in statistics and seeing the patterns that are prevelant in the real world and in math is astounding. the usefullness of a normal distribution in statistics as well the simplicity with which his equations can be used to see the probabilities of the world around us is fantastical. 
  

