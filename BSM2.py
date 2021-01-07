import datetime as dt
from datetime import date, timedelta
from scipy.stats import norm
from datetime import timedelta
import pandas_datareader.data as web
import numpy as np

# inputting ticker for option evaluation
tick = str(input('Enter Ticker: ')).upper()

# global variable for current date
now = dt.datetime.now()

# strike price that you want to find value for
strike = float(input('Enter Strike Price: '))

# finding time to maturity for options within one year
def TTM():
    date_ent = (input('Enter date of expiration(YYYY,MM,DD): '))
    # format datetime information for valuation
    year, month, day = map(int, date_ent.split(','))
    mat = dt.datetime(year, month, day)
    end = now

    # converting to whole number days
    day_to_m = (mat - end).days

    # returning values standardized to one-year
    return float((day_to_m)/252)

# make global variable to save computational tax
d2m = TTM()

# finding weekly, monthly and annualized vol for BSM calculation
def find_vol():
    # indexed start end datetime for annualized returns
    end = now
    start = now - timedelta(days=252)

    # collecting Adj Close data for inputted ticker
    stock = web.DataReader(tick, 'yahoo', start, end)['Adj Close']

    # yearly returns of stock data
    log_ret = np.log(stock) - np.log(stock).iloc[0]

    # standard deviation from log returns
    std = np.std(log_ret)

    return std

def d1_and_d2():
    # one year treasury rate
    r = .0015
    # inputtng strike price
    K = strike

    # indexing datetime for underlying asset
    end = now
    start = now - timedelta(days=2)

    # getting current day trading price for underlying
    stock = web.DataReader(tick, 'yahoo', start, end)['Adj Close']
    S = stock[0]

    # defining days and vol from prior functions
    vol = find_vol()
    days = d2m

    # finding inputs for bsm model
    d1 = (np.log(S / K) + (r + ((vol**2) / 2)) * (days)) / (vol * np.sqrt(days))
    d2 = (np.log(S / K) + (r - ((vol**2) / 2)) * (days)) / (vol * np.sqrt(days))

    return d1, d2, S

# bsm for call option
def BSM():
    # pulling information from prior functions for variables in BSM
    K = strike
    S = d1_and_d2()[2]
    r = .0015
    days = d2m

    # finding European call
    call = (S*(norm.cdf(d1_and_d2()[0]))) - K * np.exp(r*days) * norm.cdf(d1_and_d2()[1])

    return call

print(BSM())
