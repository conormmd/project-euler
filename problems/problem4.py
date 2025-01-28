import numpy as np
import utils.utils as utils

class PalindromeProduct:

    def __init__(self, num_digits):
        self.num_digits = num_digits

        self.number_limit_max = 0
        self.number_limit_min = 0
        self.limit_max = 0
        self.limit_min = 0
        self.factors = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.get_product_limits()
        self.get_palindromes()
        print(self.answer)
        print(self.factors)

    def get_product_limits(self):
        self.number_limit_max = int('9'*self.num_digits)
        self.limit_max = self.number_limit_max**2

        self.number_limit_min = int('1'+'0'*(self.num_digits-1))
        self.limit_min = self.number_limit_min ** 2

    def get_palindromes(self):
        for number in range(self.limit_max, self.limit_min, -1):
            if utils.check_if_palindrome(number):
                factors = utils.get_factors(number, [self.number_limit_min, self.number_limit_max+1])
                if self.check_valid_factors(factors):
                    self.answer = number
                    break
                else:
                    continue
            else:
                continue

    def check_valid_factors(self, factors):
        if len(factors) == 0:
            return False
        for factor_pair in factors:
            if (min(factor_pair) >= self.number_limit_min) & (max(factor_pair) <= self.number_limit_max):
                self.factors = factor_pair
                return True
            else:
                continue
        return False

if __name__ == '__main__':
    num_digits = 3
    PalindromeProduct(num_digits)
