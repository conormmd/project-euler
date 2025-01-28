import utils.utils as utils
import numpy as np

class CircularPrimes:

    def __init__(self, limit):
        self.limit = limit

        self.circular_primes = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.get_circular_primes()
        self.answer = len(self.circular_primes)
        print(self.answer)

    def get_circular_primes(self):
        for number in range(2, limit):
            if utils.check_if_prime(number):
                if self.check_if_circular(number):
                    self.circular_primes.append(number)
                else:
                    continue
            else:
                continue

    @staticmethod
    def check_if_circular(candidate):
        candidate = str(candidate)

        for rotation in range(1,len(candidate)):
            candidate = candidate[-1] + candidate[:-1]

            if utils.check_if_prime(int(candidate)):
                continue
            else:
                return False

        return True

if __name__ == '__main__':
    limit = 1000000
    CircularPrimes(limit)
