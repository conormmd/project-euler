import math
import numpy as np

class ReciprocalCycle:

    def __init__(self, limit, num_digits):
        self.limit = limit
        self.num_digits = num_digits

        self.reciprocal = ''
        self.answer_pattern = ''
        self.answer = 1

        self.get_answer()

    def get_answer(self):
        self.check_reciprocal_to_limit()
        print(self.reciprocal)
        print(self.answer_pattern)
        print(self.answer)

    def check_reciprocal_to_limit(self):
        for number in range(1, self.limit):
            reciprocal = self.manual_long_divison(1, number, self.num_digits)
            # Anything with length < num_digits is not reciprocal
            if len(reciprocal) != self.num_digits:
                continue
            else:
                pattern, reciprocal_fmt = self.check_reciprocal_for_cycle(reciprocal)
                print(number, len(pattern))
                print(pattern)
                if len(pattern) > self.answer:
                    self.reciprocal = reciprocal
                    self.answer_pattern = pattern
                    self.answer = number


    def check_reciprocal_for_cycle(self, reciprocal):
        # TODO - Rework to iterate while adding digits to the manual long division
        decimal = reciprocal[2:]
        # clip the string at different starting positions to skip starting non-patterns
        # e.g. 166666 does not have a pattern, clip the 1 -> 66666 has a pattern
        for starting_pos in range(len(decimal)):
            decimal_clipped = decimal[starting_pos:]
            # select a window size to try and find a pattern
            # e.g. 666666, window 1 -> 6, window starting size set as self.answer to skip early checks
            for window in range(1, int(len(decimal_clipped)/2) - 1):
                substring = decimal_clipped[:window]

                # look at subsequent window sized sections of the string to see if pattern exists. ignore end section if less than window size
                # e.g. 123123123, window size 3, 123 123 123 all match the substring 123
                fail_flag = False
                for i in range(len(decimal_clipped)//window):
                    section = decimal_clipped[i * window: (i + 1) * window]
                    if len(section) < window:
                        break
                    elif substring == section:
                        continue
                    else:
                        fail_flag = True
                        break

                if fail_flag is False:
                    return substring, f'0.{decimal[:starting_pos]}({substring})'

        return None, None

    @staticmethod
    def manual_long_divison(numerator, denominator, num_digits):
        answer = ''
        while len(answer) < num_digits:
            divisor = numerator // denominator
            remainder = numerator % denominator

            if (answer == '') & (remainder == 0):
                answer += str(divisor)
                break
            elif answer == '':
                answer += str(divisor) + '.'
            else:
                answer += str(divisor)

            if remainder == 0:
                break
            else:
                numerator = remainder * 10

        return answer

if __name__ == '__main__':
    limit = 1000
    num_digits = 100000
    ReciprocalCycle(limit, num_digits)
