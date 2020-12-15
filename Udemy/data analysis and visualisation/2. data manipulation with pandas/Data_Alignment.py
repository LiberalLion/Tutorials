import  numpy as np
import pandas as pd
from pandas import Series,DataFrame

series1 = Series([100,200,300],index=['A','B','C'])
series2 = Series([300,400,500,600],index=['A','B','C','D'])

#sum of series
print "Sum of Series=",series1+series2

#dataframe
df1 = DataFrame(np.arange(4).reshape(2,2),index=['Car','Bike'],columns=['A','B'])
df2 = DataFrame(np.arange(9).reshape(3,3),index=['Car','Bike','Boat'],columns=['A','B','C'])
print "Df1\n",df1
print "Df2\n",df2
print "Sum of DataFrames\n",df1+df2

#substitution
df1 = df1.add(df2,fill_value=0)
print df1 

series3 = df2.ix[0]
print df2 - series3
