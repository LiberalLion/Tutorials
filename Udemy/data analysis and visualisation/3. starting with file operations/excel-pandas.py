import pandas as pd

#exlrd
#openpyxl

excelfile = pd.ExcelFile('demo2.xlsx')
df = excelfile.parse('demo2')
print df
