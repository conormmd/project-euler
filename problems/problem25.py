import numpy as np
import utils.utils as utils

class FibonacciNumberLen:

    def __init__(self, limit):
        self.limit = limit

        self.fibonacci = [1, 1]
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_fibonacci()
        self.answer = len(self.fibonacci)
        print(self.answer)

    def generate_fibonacci(self):
        while len(str(self.fibonacci[-1])) < self.limit:
            self.fibonacci.append(self.fibonacci[-1] + self.fibonacci[-2])


if __name__ == '__main__':
    limit = 1000

    FibonacciNumberLen(limit)


