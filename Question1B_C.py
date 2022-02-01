'''
Question 1 - b

'''
import pandas 
import numpy as np
import datascience

name = ['Abe', 'Abhay','Acelin','Adelphos']
data = {'Student ID':['V001','V002','V003','V004'],
'Name':['Abe', 'Abhay','Acelin','Adelphos'],
'Total Marks':[95,80,74,81]}



df = pandas.DataFrame(data = data)

df

SeriesOne = pandas.Series(df['Name'])
S1 = SeriesOne.str.contains('e', regex = False)
table2 = pandas.DataFrame(data = S1 )

TableMerge = pandas.merge(df, table2, left_index = True, right_index = True)
TableMerge

containsE = TableMerge[TableMerge['Name_y']==True]
Elist = containsE['Name_x'].tolist()
for i in range (len(Elist)):
    Elist[i] = Elist[i].upper()
print('Names that contain the letter E', Elist)

average = sum(containsE['Total Marks'])/len(containsE)
print('The average score for students with an E in their name is', average)

averagelower = sum(TableMerge['Total Marks'])-sum(containsE['Total Marks'])/(len(TableMerge)-len(containsE))
print('The average score for those who do not have an "E" in their name is', averagelower)