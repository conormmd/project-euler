import utils.utils as utils
import numpy as np

class MaxPathSum:

    def __init__(self, triangle_raw):

        self.triangle_list = list()
        self.triangle_flat = list()
        self.process_triangle(triangle_raw)

        self.path = None
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.find_path()
        self.answer = np.sum(self.path)
        print(self.path)
        print(self.answer)

    def process_triangle(self, triangle_raw):
        triangle_list = [row.split(' ') for row in triangle_raw.split('\n') if row != '']

        self.triangle_list = [[int(item) for item in row] for row in triangle_list]
        self.triangle_flat = [item for row in triangle_list for item in row]

    def find_path(self):
        # Start from bottom row up
        # Look at each pair of values and select the highest of the two and add it to a running total
        # Move to the next row above and do the same
        cached_paths = []
        for iteration, row in enumerate(self.triangle_list[::-1]):
            cached_paths_temp = []

            # If at the top of the triangle, update the last remaining cached path and exit
            if len(row) == 1:
                self.path = row + cached_paths[0]

            for pair_index in range(len(row) - 1):
                # For first iteration (bottom row) there is no cached path
                if iteration == 0:
                    left_path = [row[pair_index]]
                    right_path = [row[pair_index + 1]]
                # For all other iterations, a cached path exists holding the highest scoring path
                else:
                    left_path = [row[pair_index]] + cached_paths[pair_index]
                    right_path = [row[pair_index + 1]] + cached_paths[pair_index + 1]

                # Create a new temporary cached path for the next iteration
                if np.sum(left_path) >= np.sum(right_path):
                    cached_paths_temp.append(left_path)
                else:
                    cached_paths_temp.append(right_path)

            # Updated cached path to reflect newly calculated path once all pairs have been checked
            cached_paths = cached_paths_temp.copy()







if __name__ == '__main__':
    triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

    MaxPathSum(triangle)
