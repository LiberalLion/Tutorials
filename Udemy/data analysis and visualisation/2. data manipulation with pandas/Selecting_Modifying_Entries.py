import numpy as np
import pandas as pd
from pandas import  Series,DataFrame

series1 = Series([100,200,300],index=['A','B','C'])
print series1

#access element of series
print series1['A']

#access multiple elements
print series1[['A','B']]

#number indexes
print series1[0] #equivalent to series1['A']

#accessing multiple elements
print series1[0:2]
print series1[0:4]

#conditional indexes
print series1[series1>150]
print series1[series1==300]

#using datframes and accessing
df1 = DataFrame(np.arange(9).reshape(3,3),index=['Car','Bike','Cycle'],columns=['A','B','C'])
print df1

#col wise
print df1['A']
print df1[['A','B']] #multiple values

print df1>5

#access elements using ix function
print df1.ix['Bike']
