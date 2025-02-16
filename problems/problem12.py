import utils.utils as utils

class TriangleFactors:

    def __init__(self, num_factors):
        self.num_factors = num_factors

        self.triangles = [1, 3]
        self.answer_factors = []
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_triangles()
        print(self.answer)

    def generate_triangles(self):
        number = 2
        while True:
            number += 1
            triangle = self.triangles[-1]+number
            self.triangles.append(triangle)

            factors = utils.get_factors(triangle, return_flat=True)
            factors = [1] + factors + [triangle]
            if len(factors) > self.num_factors:
                self.answer = triangle
                self.answer_factors = factors
                break

if __name__ == '__main__':
    num_factors = 500
    TriangleFactors(num_factors)

