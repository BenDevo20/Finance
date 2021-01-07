"""
often interpreted as the market's expectation for the future vol of a stock and is implied by the price of the stocks
options

implied vol is not observable in the market but can be derived from the price of an option
vol is an input parameter in the option pricing model

use the bisection method to solve the BSM pricing equation and find the root which is the implied vol
"""

import numpy as np
import scipy
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import timedelta

end = dt.datetime.now()
start = end - timedelta(days=1500)

tick = ['SPY']
spy = web.DataReader(tick, 'yahoo', start, end)['Adj Close']

# setting parameters
# first oder difference
r = np.diff(np.log(spy))

# mean
r_mean = np.mean(r)

# diff squares
diff_square = [(r[i] - r_mean)**2 for i in range(0, len(r))]

# standard deviation
std = np.sqrt(np.sum(diff_square)*(1.0/(len(r) - 1)))

# vol
vol = std * np.sqrt(252)
print(vol)