"""
interest rate derivatives are popular with investors who require customized cash flow needs
Vasicek model, CIR model, and Hull-White model are popular pricing procedures that have been under academic studies

Coupon bonds are quoted as a percentage of par value on an annual basis
Normal environment - long-term interest rates are higher than short term interest rates

inverted yeild curve - long term interest rates are lower that short-term
this occurs when the supply of money is tight - investors want to preserve their money in the short term
negative interest rates may be observed - where the inflation rate exceeds the payout of interest rate products

"""

# valuing a zero-coupon bond
"""
zero-coupon does not pay any periodic interest except on maturity - par value is repaid
"""

def zero_coupon(par, y, t):
    """
    :param par: face value of the bond
    :param y: annual yield or rate of the bond
    :param t: time to maturity in years
    :return: value of a zero coupon bond
    """
    return par / (1+y)**t

