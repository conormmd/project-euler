class SumSquareDifference:

    def __init__(self, limit):
        self.limit = limit

        self.sum_of_squares = 0
        self.square_of_sum = 0
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.get_sum_and_square()
        self.answer = self.square_of_sum - self.sum_of_squares
        print(self.answer)

    def get_sum_and_square(self):
        sum_regular = 0
        sum_squares = 0
        for number in range(1, self.limit+1):
            sum_regular += number
            sum_squares += number**2

        self.sum_of_squares = sum_squares
        self.square_of_sum = sum_regular**2


if __name__ == '__main__':
    limit = 100
    SumSquareDifference(limit)
