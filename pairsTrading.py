import numpy as np
import pandas as pd
import statsmodels
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt

"""
Pair of securities (X,Y) that have an underlying economic link 
Can model this economic link with a mathematical model - you can make trades on it 
"""

# generating two fake securities as example of p-trading
# model x's daily return by drawing from a normal distribution - perform cumulative sum to get the value of X for each day
X_returns = np.random.normal(0, 1 , 100)
X = pd.Series(np.cumsum(X_returns), name = 'X') + 50

# Generating Y has to have an economic link to X - price of Y shouldnt vary too significantly
some_noise = np.random.normal(0, 1, 100)
Y = X + 5 + some_noise
Y.name = 'Y'
pd.concat([X, Y], axis=1)

"""
Cointegration of the two series 
there is some linear combination between them that will vary around a mean - the combo between them is related to the 
same probability distribution
"""

spread = (Y-X)
# testing for cointegration
score, pvalue, _ = coint(X,Y)
print(pvalue)

"""
Hedging - method for finding viable pairs all live on a spectrum 
multiple comparison bias is the increased chance to incorrectly generate a sginificant p-value when many tests are run 
"""

def find_cointegrated_pairs(data):
    n = data.shape[1]
    score_matrix = np.zeros((n,n))
    pvalue_matrix = np.ones((n,n))
    keys = data.keys()
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            S1 = data[keys[i]]
            S2 = data[keys[j]]
            results = coint(S1, S2)
            score = results[0]
            pvalue = results[1]
            score_matrix[i, j] = score
            pvalue_matrix[i, j] = pvalue

            if pvalue < 0.05:
                pairs.append((keys[i], keys[j]))
    return score_matrix, pvalue_matrix, pairs

"""

"""