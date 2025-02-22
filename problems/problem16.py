import utils.utils as utils
import numpy as np

class PowerDigitSum:

    def __init__(self, power, base):
        self.power = power
        self.base = base

        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.answer = np.sum(int(n) for n in str(self.base**self.power))
        print(self.answer)


if __name__ == '__main__':
    power = 1000
    base = 2

    PowerDigitSum(power, base)
