"""
Spot - represent current interest rates for several maturities
zero - represent the internal rate of return of zero-coupon
"""

# bootstrapping the yield curve
import math

class BootstrapYieldCurve():
    def __init__(self):
        # map each T to a zero rate
        self.zero_rates = dict()
        # map each T to an instrument
        self.instruments = dict()

    def add_instrument(self, par, T, coup, price, comp_freq=2):
        self.instruments[T] = (par, coup, price, comp_freq)

    def get_zero_rates(self):
        # calc the list of available zero rates
        self.__bootstrap_zero_coup__()
        self.__get_bond_spot_rates__()
        return [self.zero_rates[T] for T in self.get_maturities()]

    def get_maturities(self):
        # return sorted maturities from added instruments
        return sorted(self.instruments.keys())

    def __bootstrap_zero_coupons__(self):
        # get zero rates from zero coupons
        for T in self.instruments.iterkeys():
            (par, coup, price, freq) = self.instruments[T]
            if coup == 0:
                self.zero_rates[T] = self.zero_coupon_spot_rate(par, price, T)
    def __get_bond_spot_rates(self):
        # get spots for every maturity available
        for T in self.get_maturities():
            instrument = self.instruments[T]
            (par, coup, price, freq) = instrument

            if coup != 0:
                self.zero_rates[T] = self.__calculate_bond_spot_rate__(T, instrument)

    def __calculate_bond_spot_rate__(self, T, instrument):
        # getting spot rate of a bond by bootstrapping
        try:
            (par, coup, price, freq) = instrument
            # number of coupon payments
            periods = T * freq
            value = price
            per_coupon = coup / freq

            for i in range(int(periods)-1):
                t = (i+1)/float(freq)
                spot_rate = self.zero_rates[t]
                discounted_coupon = per_coupon * math.exp(-spot_rate*t)
                value -= discounted_coupon

            # derving spot rate for a particular maturity
            last_per = int(periods) / float(freq)
            spot_rate = -math.log(value / (par+per_coupon)) / last_per
            return spot_rate

        except:
            print('error: spot rate not found')

    def zero_coupon_spot_rate(self, par, price, T):
        # getting zero rate of a zero coupon bond
        spot_rate = math.log(par/price) / T
        return spot_rate

