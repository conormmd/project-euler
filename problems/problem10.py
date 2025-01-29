import utils.utils as utils
import numpy as np

class SieveOfEratosthenes:

    def __init__(self, limit):
        self.limit = limit

        self.primes = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.primes = utils.sieve_of_eratosthenes(self.limit)
        self.answer = np.sum(self.primes)
        print(self.answer)


if __name__ == '__main__':
    limit = 2000000
    SieveOfEratosthenes(limit)


