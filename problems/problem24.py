import math
import numpy as np

class LexicographicPermutations:

    def __init__(self, digits, n):
        self.digits = self.order_digits_list(digits)
        self.n = n
        self.answer = ''

        self.get_answer()

    def get_answer(self):
        self.select_digit(self.digits)
        print(self.answer)

    def select_digit(self, digits, n_running=0):
        for digit in digits:
            # check this digit has not been used already:
            if digit in self.answer:
                continue
            # max_perms available if this digit is selected
            max_perms = math.factorial(len(digits) - 1)

            # if skipping this digit will exceed nth permutation, set digit and repeat for the remaining digits
            if n_running + max_perms >= self.n:
                self.answer += digit
                digits.remove(digit)
                # repeat for remaining available digits
                self.select_digit(digits, n_running)
                break
            # if still below nth permutation, continue with next digit
            else:
                n_running += max_perms


    @staticmethod
    def order_digits_list(digits):
        return sorted(list(digits))

if __name__ == '__main__':
    digits = '1234567890'
    n = 1e6
    LexicographicPermutations(digits, n)
