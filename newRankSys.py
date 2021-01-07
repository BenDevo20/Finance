import pandas as pd
import numpy as np

xls = pd.ExcelFile('RankingChange.xlsx')
df1 = pd.read_excel(xls, 'rank').dropna(axis=1)
xls