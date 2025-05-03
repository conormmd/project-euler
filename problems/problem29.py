import math
import numpy as np
import utils.utils as utils

class DistinctPowers:

    def __init__(self, lims):
        self.lower_lim = lims[0]
        self.upper_lim = lims[1]

        self.results = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_powers()
        self.answer = len(self.results)
        print(self.answer)

    def generate_powers(self):
        # 4**2 = (2**2)**2 = 2**4
        # Break base (a) down into prime factors and eliminate

        # base
        for a in range(self.lower_lim, self.upper_lim + 1):
            prime_factors = utils.get_prime_factors(a)
            simplified = utils.simplify_prime_factors(prime_factors)
            # power
            for b in range(self.lower_lim, self.upper_lim + 1):
                result =  [(factor[0], factor[1]*b) for factor in simplified]
                if result in self.results:
                    pass
                else:
                    self.results.append(result)

    # int overflow
    # def generate_powers(self):
    #     a = np.array(range(self.lower_lim, self.upper_lim + 1), dtype=np.int64)
    #     for b in range(self.lower_lim, self.upper_lim + 1):
    #         self.results.extend(np.power(a, b))


if __name__ == '__main__':
    lims = (2, 100)

    DistinctPowers(lims)
