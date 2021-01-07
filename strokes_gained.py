import numpy as np
import pandas as pd
import sklearn
import statsmodels.api as sm
from statsmodels import regression
import matplotlib.pyplot as plt

StrData = pd.ExcelFile('Golf-Regression(New).xlsx')
df1 = pd.read_excel(StrData, 'Overall Data')
df2 = pd.read_excel(StrData, 'Strokes Gained Data')

print(df2)

