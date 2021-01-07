"""
generating a list of forward rates from list of spot rates
"""

class ForwardRates(object):
    def __init__(self):
        self.forward_rates = []
        self.spot_rates = dict()

    def add_spot_rate(self, T, spot_rate):
        self.spot_rates[T] = spot_rate

    def __calculate_forward_rate__(self, T1, T2):
        R1 = self.spot_rates[T1]
        R2 = self.spot_rates[T2]
        forward_rate = (R2*T2 - R1*T1) / (T2 - T1)
        return forward_rate

    def get_forward_rates(self):
        periods = sorted(self.spot_rates.keys())
        for T2, T1 in zip(periods, periods[1:]):
            forward_rate = self.__calculate_forward_rate__(T1, T2)
            self.forward_rates.append(forward_rate)

        return self.forward_rates
