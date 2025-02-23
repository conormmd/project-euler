import math
import numpy as np
import utils.utils as utils

class NonAbundantNumbers:

    def __init__(self, start, limit):
        self.start = start
        self.limit = limit

        self.sample_space = None
        self.abundant = list()
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_sample_space()
        self.generate_abundant()
        self.check_if_sum_of_two_abundant()
        self.answer = np.sum(idx for idx, is_sum_of_two_abundant in enumerate(self.sample_space) if is_sum_of_two_abundant == False)
        print(self.answer)

    def check_if_sum_of_two_abundant(self):
        for abundant_1 in self.abundant:
            for abundant_2 in self.abundant:
                abundant_sum = abundant_1 + abundant_2
                if abundant_sum <= self.limit:
                    self.sample_space[abundant_sum] = True
                else:
                    pass

    def generate_abundant(self):
        for number in range(12, self.limit - 12 + 1):
            if self.check_if_abundant(number):
                self.abundant.append(number)
            else:
                pass

    def generate_sample_space(self):
        self.sample_space = np.zeros(limit+1, dtype=np.bool)

    @staticmethod
    def check_if_abundant(number):
        if utils.get_sum_of_proper_divisors(number) > number:
            return True
        else:
            return False

if __name__ == '__main__':
    start = 24
    limit = 28123

    NonAbundantNumbers(start, limit)
