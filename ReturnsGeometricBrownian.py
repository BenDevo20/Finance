import math
import numpy as np
import pandas as pd
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'serif'
import datetime as dt


# probability density function of a normal random variable x
def dN(x, mu, sigma):
    ''' Probability density function of a normal random variable x.
    Parameters
    mu: float expected value
    sigma: float standard deviation
    pdf: float value of probability density function
    '''
    z = (x - mu) / sigma
    pdf = np.exp(-0.5 * z ** 2) / math.sqrt(2 * math.pi * sigma ** 2)
    return pdf

# simulate a number of years of daily stock returns
def sim_gbm():
    # model params
    S0 = 100.0 # initial index level
    T = 10.0 # time horizon
    r = 0.05 # riskless free rate
    vol = 0.2 # instantaneous vol

    # simulation params
    np.random.seed(250000)
    # dates for the simulation
    dates = pd.DatetimeIndex(start = '30-09-2004', end = '30-09-2014', freq='B')
    M = len(dates)
    I = 1 # index level paths
    dt = 1/252 # fixed time for simplicity - 252 trading days in a year
    df = math.exp(-r*dt) # discount factor

    # stock price paths
    rand = np.random.standard_normal((M, I))
    S = np.zeros_like(rand) # stock matrix
    S[0] = S0
    for t in range(1,M):
        S[t] = S[t-1] * np.exp((r * vol**2 / 2) * dt + vol * rand[t] * math.sqrt(dt))
    gbm = pd.DataFrame(S[:, 0], index=dates, columns=['index'])
    gbm['Returns'] = np.log(gbm['index'] / gbm['index'].shift(1))

    # realized volatility
    gbm['rea_var'] = 252*np.cumsum(gbm['Returns']**2) / np.arange(len(gbm))
    gbm['rea_vol'] = np.sqrt(gbm['rea_var'])
    gbm = gbm.dropna()
    return gbm

