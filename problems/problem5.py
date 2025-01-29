import numpy as np
import utils.utils as utils

class SmallestMultiple:

    def __init__(self, limit):
        self.limit = limit

        self.prime_factors = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.get_common_prime_factors_to_limit()
        self.answer = np.prod(self.prime_factors)
        print(self.answer)

    def get_common_prime_factors_to_limit(self):
        for number in range(2, self.limit+1):
            prime_factors = utils.get_prime_factors(number)
            self.prime_factors = utils.combine_prime_factors(self.prime_factors, prime_factors)

if __name__ == '__main__':
    limit = 20
    SmallestMultiple(limit)
