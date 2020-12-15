import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = pd.read_csv('demo with header.csv')
print df

df = pd.read_csv('demo without header.csv', header=None) #used when there is no topic name
print df.head()

#using readtable of pandas
# FutureWarning: read_table is deprecated, use read_csv instead
df2 = pd.read_table('demo without header.csv',sep=',',header=None)
print df

#reading partial rows of a csv file # partial row importing
print pd.read_csv('demo without header.csv',nrows=2,header=None)

#dumping data into a new csv file
df2.to_csv('Output_csv.csv',sep='!');

#selecting specific column of a csv file
df.to_csv('Data_Output.csv',columns=[0,1])
