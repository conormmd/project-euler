import math
import numpy as np

class SpiralDiagonals:

    def __init__(self, dimension):
        self.dimension = dimension

        self.diagonals = [1]
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.simulate_diagonals()
        self.answer = np.sum(self.diagonals)
        print(self.answer)

    def simulate_diagonals(self):
        # Diagonals start at bottom right and go clockwise
        # Each concentric square is odd numbered and length l, and each diagonal is l-1 away from the next
        # Jumping between squares l_1 -> l_2 requires a jump of l_2-1

        for l in range(3, self.dimension + 1, 2):
            for c in range(4):
                self.diagonals.append(self.diagonals[-1] + l - 1)


if __name__ == '__main__':
    dimension = 1001

    SpiralDiagonals(dimension)
