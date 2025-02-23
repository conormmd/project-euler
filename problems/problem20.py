import math
import numpy as np

class FactorialDigitSum:

    def __init__(self, number):
        self.number = number

        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.answer = np.sum(int(n) for n in str(math.factorial(self.number)))
        print(self.answer)


if __name__ == '__main__':
    number = 100

    FactorialDigitSum(number)
