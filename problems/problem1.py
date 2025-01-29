import utils.utils as utils

class MultiplesOfFactors:

    def __init__(self, factors, limit):

        self.factors = factors
        self.limit = limit

        self.multiples = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.get_multiples_below_limit()
        self.get_sum_of_multiples()
        print(self.answer)

    def check_factors(self, number):
        factor_check = [utils.check_if_multiple(number, factor) for factor in self.factors]
        return bool(sum(factor_check))

    def get_multiples_below_limit(self):
        for number in range(0, self.limit):
            if self.check_factors(number):
                self.multiples.append(number)
            else:
                pass

    def get_sum_of_multiples(self):
        self.answer = sum(self.multiples)

if __name__ == '__main__':
    factors = [3, 5]
    limit = 1000

    MultiplesOfFactors(factors, limit)
