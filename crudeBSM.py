import pandas as pd
import pandas_datareader.data as web
import numpy as np
import math
import datetime as dt
from datetime import timedelta
from scipy.stats import norm
import matplotlib.pyplot as plt

# setting end time to rolling day
end = dt.datetime.now()

# start time end - 252 days (rolling year)
start = end - timedelta(days=252)
forward = dt.datetime

# enter ticker of the stock that want to find the option price for
tick = str(input('Enter Ticker: ')).upper()

# pulling data from yahoo finance using pandas api
stock = web.DataReader(tick, 'yahoo', start, end)['Adj Close']
df = pd.DataFrame(stock)

# finding log returns of the underlying
log_ret = np.log(stock) - np.log(stock).iloc[0]

plt.plot(log_ret)
plt.show()
#print(log_ret)

# finding vol from standard deviation of year log returns
std = np.std(log_ret)
#print(std)

# generate index of forward dates for potential options -- limited to 100
num = 100
forw_date = [end - timedelta(days=x) for x in range(num)]

# finding d1 and d2 for the CDF for guassian distro
def d1_and_d2(X, r):
    T = end
    t = forw_date[10]
    S = stock[171]
    vol = std
    days = float((T-t).days)

    d1 = (math.log(S / X) + (r + ((vol**2) / 2)) * (days)) / (vol * np.sqrt(days))
    d2 = (math.log(S / X) + (r - ((vol**2) / 2)) * (days)) / (vol * np.sqrt(days))

    return d1, d2

# BSM for non-dividend paying stock
def BSM(X, r):
    T = end
    t = forw_date[10]
    S = stock[171]
    days = float((T-t).days)

    call = (norm.cdf(d1_and_d2(X, r)[0]) * S) - norm.cdf(d1_and_d2(X, r)[1]) * X * np.exp(-1*r*days)
    return call, days


print(BSM(1600, 0.00))