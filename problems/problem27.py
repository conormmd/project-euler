import numpy as np
import utils.utils as utils

class QuadraticPrimes:

    def __init__(self, limit_a, limit_b):
        self.limit_a = limit_a
        self.limit_b = limit_b

        self.max_n = 0
        self.max_pair = 0
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_candidates_within_lim()
        self.answer = self.max_pair[0] * self.max_pair[1]
        print(self.max_n)
        print(self.max_pair)
        print(self.answer)

    def generate_candidates_within_lim(self):
        # Filter out immediate failures - case when n = 0 -> func = b < 2
        for b in range(2, self.limit_b + 1):
            for a in range((-1 * self.limit_a) + 1, self.limit_a):
                # We know that 39 is known max so lets add a single check for 40 to potentially save time

                if utils.check_if_prime(self.remarkable_quadratic(39, a, b)) is False:
                    continue

                max_n = self.evaluate_candidate_quadratic(a, b)

                if max_n > self.max_n:
                    self.max_n = max_n
                    self.max_pair = (a, b)

    def evaluate_candidate_quadratic(self, a, b):
        n = 0
        prime = True

        while prime is True:
            n += 1
            product_n = self.remarkable_quadratic(n, a, b)
            prime = utils.check_if_prime(product_n)

        return n

    @staticmethod
    def remarkable_quadratic(n, a, b):
        return n**2 + a * n + b


if __name__ == '__main__':
    limit_a = 1000
    limit_b = 1000

    QuadraticPrimes(limit_a, limit_b)
