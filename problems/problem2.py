import numpy as np
import utils.utils as utils


class FibonacciNumbers:

    def __init__(self, limit):
        self.limit = limit

        self.fibonacci = [1, 1]
        self.evens = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_fibonacci()
        self.get_evens_in_fibonacci()
        self.get_sum_of_evens()
        print(self.answer)

    def generate_fibonacci(self):
        while self.fibonacci[-1] < self.limit:
            self.fibonacci.append(self.fibonacci[-1] + self.fibonacci[-2])

    def get_evens_in_fibonacci(self):
        for number in self.fibonacci:
            if utils.check_if_even(number):
                self.evens.append(number)
            else:
                pass

    def get_sum_of_evens(self):
        self.answer = sum(self.evens)


if __name__ == '__main__':
    limit = 4000000

    FibonacciNumbers(limit)


