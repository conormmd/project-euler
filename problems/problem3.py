import numpy as np
import utils.utils as utils

class PrimeFactors:

    def __init__(self, number):
        self.number = number

        self.prime_factors = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.answer = self.get_largest_prime_factor(self.number)
        print(self.answer)

    def get_answer_alt(self):
        self.prime_factors = utils.get_factors_which_are_prime(self.number)
        self.answer = max(self.prime_factors)
        print(self.answer)

    @staticmethod
    def get_largest_prime_factor(number):
        check_limit = int(np.sqrt(number))
        prime_factors = []

        for factor in range(2, check_limit + 1):
            if number % factor == 0:
                factor_1 = factor
                factor_2 = number / factor

                if utils.check_if_prime(factor_1):
                    prime_factors.append(factor_1)

                # If factor_2 is prime, the first instance it is will always be the largest prime
                if utils.check_if_prime(factor_2):
                    return factor_2

        return max(prime_factors)


if __name__ == '__main__':
    number = 600851475143
    PrimeFactors(number)
