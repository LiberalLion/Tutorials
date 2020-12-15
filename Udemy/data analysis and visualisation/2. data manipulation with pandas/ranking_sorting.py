import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

series1 = Series([500,1000,1500],index=['a','c','b'])
print series1

#sorting by index
print series1.sort_index()

#sorting by values
print series1.sort_values()

#ranking of series
print series1.rank()
series2 = Series(randn(10))
print series2

print series2.rank()
