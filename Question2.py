import pandas as pd
import numpy as np
import statistics

#read in .csv Data
df = pd.read_csv('TrimbleData.csv')
df.head(5)

#check for length, min and max. this helps to set up the graph when we are there, and to make sure that all of the data was read in. 
print('total values:', len(df)+1)
s1 = df['23.82729036706873'].to_list()
print('Range', min(s1),max(s1))

#import visualization tools

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

bins = 50

#histogram
plots.hist(s1, bins = bins)

#The graph shows us that the information is normaly distributed between 11 and 34. 