import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels import regression
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

# importing data
golfData = pd.read_excel('Golf-Regression(New).xlsx')

# finding average distance of all players in the top 100
mean = golfData['Average Drive'].mean()

# finding the different between individual golfer drive and mean
golfData['PlusMinusAvg'] = golfData['Average Drive'] - mean

# creating variables for linear regression
# dependent variable - overall rank of the player
y = golfData['owgr_rank']

# longest drive of individual player
PMA = golfData['PlusMinusAvg']

# percent of greens hit from approach shots
GFP = golfData['GPF']

# one-putt percentage of individual players
OPP = golfData['OPP']

#  Interaction term between OPP and GFP
#golfData['Interaction'] = golfData['GPF'] * golfData['OPP']
#INT = golfData['Interaction']

# add constant - default for Statsmodels is no constant
X = sm.add_constant(np.column_stack((PMA, GFP, OPP)))

# fitting regression model to independent and dependent variables
mlr = regression.linear_model.OLS(y, X).fit()

prediction = mlr.params[0] + mlr.params[1]*PMA + mlr.params[2]*GFP + mlr.params[3]*OPP
prediction.name = 'World Rank Prediction'
print(mlr.summary())

"""# graphing regression
PMA.plot()
GFP.plot()
OPP.plot()
y.plot()
prediction.plot(color='r')
plt.legend(bbox_to_anchor=(1,1), loc=2)
plt.show()
"""