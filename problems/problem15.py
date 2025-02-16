import utils.utils as utils
import numpy as np

class LatticePaths:

    def __init__(self, grid_shape):
        self.grid_x = grid_shape[0]
        self.grid_y = grid_shape[0]

        self.vector_len = self.grid_x + self.grid_y
        self.solutions = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        # How many ways can I arrange x 1s and y 0s? -> binomial
        self.answer = self.combinations()
        print(self.answer)

    def combinations(self):
        n = self.vector_len
        k = self.grid_x
        return np.math.factorial(n)/(np.math.factorial(n-k)*np.math.factorial(k))

    def iterate_paths(self):
        # Run through iteration 0 (starting path)
        iteration = 0
        array = self.get_starting_path()
        sym_array = 1 - array

        self.solutions.append(array)
        self.solutions.append(sym_array)

        # Iterate through x and turn that x value from horizonal -> vertical
        for x in range(self.grid_x):
            array[x] = 0

            # Iterate through y and turn ONLY y value from vertical -> horizonal
            for y in range(self.grid_y):
                iteration += 1
                y += self.grid_x

                array_temp = array.copy()

                array_temp[y] = 1

                if array_temp not in self.solutions:
                    sym_array_temp = 1 - array_temp
                    self.solutions.append(array_temp)
                    self.solutions.append(sym_array_temp)


    def get_starting_path(self):
        # 1 is horizontal to the right
        horiz = [1] * self.grid_x
        # 0 is down
        vert = [0] * self.grid_y
        # Starting array should be horizontal to the edge, and then down
        return np.array(horiz + vert)


if __name__ == '__main__':
    grid_shape = (20, 20)
    LatticePaths(grid_shape)
