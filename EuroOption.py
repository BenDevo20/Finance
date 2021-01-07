from math import exp, log, pi, sqrt


def norm_pdf(x):
    # standard normal distribution probability density function
    return (1.0/((2*pi)**0.5))*exp(-0.5*x*x)


# approximation to the cumulative distribution function for the standard normal distribution
def norm_cdf(x):
    k = 1.0/(1.0+0.2316419*x)
    k_sum = k * (0.319381530 + k * (-0.356563782 + k * (1.781477937 + k * (-1.821255978 + 1.330274429 * k))))

    if x >= 0.0:
        return (1.0 - (1.0 / ((2 * pi)**0.5)) * exp(-0.5 * x * x) * k_sum)
    else:
        return (1.0 - norm_cdf(-x))

def d_j(j, S, K, r, v, T):
    return (log(S/K) + (r + ((-1)**(j-1))*0.5*v*v)*T)/(v*(T**0.5))
"""
price of a euro call option strike at K, with spot S, risk free r, constant vol v 
vol is over the time period to expiration and time to maturity T
"""
def vanilla_call_price(S, K, r, v, T):
    return S * norm_cdf(d_j(1, S, K, r, v, T)) - K * exp(-r*T) \
           * norm_cdf(d_j(2, S, K, r, v, T))

