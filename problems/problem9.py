import utils.utils as utils
import numpy as np

class PythagoreanTriplet:

    def __init__(self, triplet_sum):
        self.triplet_sum = triplet_sum

        self.eligible_squares = []
        self.triplets = []
        self.answer_triplet = ()
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.generate_triplets()
        self.answer = np.prod(self.answer_triplet)
        print(self.answer_triplet)
        print(self.answer)

    def generate_triplets(self):
        a=0
        b=0
        c=0

        while True:
            a += 1

            if a >= self.triplet_sum:
                break

            while True:
                b += 1

                if b >= a:
                    b=0
                    break

                c2 = a**2 + b**2
                c = int(np.sqrt(c2))

                if utils.check_if_square(c2):
                    self.triplets.append((a, b, c))

                    if a+b+c == self.triplet_sum:
                        self.answer_triplet = (a, b, c)

                if a+b+c > self.triplet_sum:
                    b=0
                    break


if __name__ == '__main__':
    triplet_sum = 1000
    PythagoreanTriplet(triplet_sum)


