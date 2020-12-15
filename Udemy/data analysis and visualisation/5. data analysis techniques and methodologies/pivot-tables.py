import numpy as np
import pandas as pd
from pandas import Series, DataFrame

url = "https://en.wikipedia.org/wiki/Pivot_table"
df_list = pd.io.html.read_html(url)
df = df_list[0]

#print df

new_header = df.iloc[0] #grabs the first row for the header
df = df[1:] #takes the data less the header row
df.columns = new_header #sets the header row as the df header

print df

print df.pivot('Data of sale', 'Sale person', 'Total price')
