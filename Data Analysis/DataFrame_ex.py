import numpy as np
import pandas as pd
from pandas import DataFrame,Series

xls=pd.ExcelFile('sample.xlsx')
#reading data from a xsl file install xslrd
DataFrame1=xls.parse('Sheet1')
print(DataFrame1)
print(DataFrame1.columns)
#to  create
DataFrame(DataFrame1,columns=['name'])
