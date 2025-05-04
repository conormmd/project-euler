import math
import numpy as np
import utils.utils as utils

class DigitFifthPowers:

    def __init__(self, power):
        self.power = power
        self.n = 1

        self.results = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.find_max_number()
        self.find_digit_powers()
        self.answer = sum(self.results)
        print(self.answer)

    def find_max_number(self):
        # Assuming all 9s, while the sum of the digit powers is greater than the number, increase the number of digits by 1
        # Stop when the number is larger than the sum of the digit powers (e.g. can't be made from a sum)
        while 9**power * self.n >= int('9' * self.n):
            self.n += 1

    def find_digit_powers(self):
        # 1 is excluded (start = 2)
        min = 2
        max = int('9' * self.n) + 1
        for number in range(min, max):
            sum_of_digit_powers = sum(int(n)**self.power for n in str(number))
            if sum_of_digit_powers == number:
                self.results.append(number)

    # int overflow
    # def generate_powers(self):
    #     a = np.array(range(self.lower_lim, self.upper_lim + 1), dtype=np.int64)
    #     for b in range(self.lower_lim, self.upper_lim + 1):
    #         self.results.extend(np.power(a, b))


if __name__ == '__main__':
    power = 5

    DigitFifthPowers(power)
