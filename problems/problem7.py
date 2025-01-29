import utils.utils as utils

class FastPrime:

    def __init__(self, nth_prime):
        self.nth_prime = nth_prime

        self.primes = [2, 3]
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.get_nth_prime()
        self.answer = self.primes[-1]
        print(self.answer)

    def get_nth_prime(self):
        while len(self.primes) < self.nth_prime:
            self.find_next_prime()

    def find_next_prime(self):
        number = max(self.primes) + 2
        while utils.check_if_prime(number) is False:
            number += 2
        self.primes.append(number)


if __name__ == '__main__':
    nth_prime = 10001
    FastPrime(nth_prime)
