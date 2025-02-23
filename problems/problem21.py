import math
import numpy as np
import utils.utils as utils

class AmicableNumbers:

    def __init__(self, limit):
        self.limit = limit
        self.sample_space = None
        self.amicable_pairs = []

        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_sample_space()
        self.generate_amicable_pair_candidates()
        self.answer = np.sum([number for pair in self.amicable_pairs for number in pair])
        print(self.answer)

    def generate_amicable_pair_candidates(self):
        for number in range(self.limit):
            if self.sample_space[number]:
                continue_flag = True
                # Non-amicable numbers will chain until they either
                # 1. Exceed the limit
                # 2. Form a closed loop or hit a previously checked number
                # 3. Generate a pair
                while continue_flag:
                    # Update number
                    self.sample_space[number] = False
                    a, b, pair_flag = self.test_candidate(number)

                    # if new number generated exceeds limit, exit while loop
                    if b > self.limit:
                        continue_flag = False
                    # if new number generated has been analysed before, exit while loop
                    elif ~self.sample_space[b]:
                        continue_flag = False
                    # if pair has been found, append pair to list, update sample space, exit while loop
                    elif pair_flag:
                        self.amicable_pairs.append((a, b))
                        self.sample_space[a] = False
                        self.sample_space[b] = False
                        continue_flag = False
                    # otherwise, update number to new candidate in chain,
                    else:
                        self.sample_space[number] = False
                        number = b

            else:
                pass

    def generate_sample_space(self):
        self.sample_space = np.ones(limit + 1, dtype=np.bool)
        self.sample_space[0] = False
        self.sample_space[1] = False

    @staticmethod
    def test_candidate(a):
        d_a = utils.get_sum_of_proper_divisors(a)
        d_b = utils.get_sum_of_proper_divisors(d_a)

        if a == d_b:
            return a, d_a, True
        else:
            return a, d_a, False


if __name__ == '__main__':
    limit = 10000

    AmicableNumbers(limit)
