import utils.utils as utils
import numpy as np

class NumberLetterCounts:
    def __init__(self, limit, start=1):
        self.limit = limit
        self.start = start

        self.suffixes = {
            0: None,
            1: 'thousand',
            2: 'million',
        }
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.calc_to_limit()
        print(self.answer)

    def calc_to_limit(self):
        for number in range(self.start, self.limit + 1):
            # Pad number so it is in triple format - e.g. 1234 -> 001234
            number = self.pad_number(number)
            # Split number into triples - e.g. 001234 -> 001, 234
            triples = [number[x * 3:  x * 3 + 3] for x in range(len(number)//3)]

            answer = []

            for num, triple in enumerate(triples):
                # Generate text for triple - e.g. 001 -> one, 234 -> two hundred and thirty-four
                triple_text = self.generate_triple_text(triple)
                # If empty, ignore
                if triple_text == '':
                    continue
                # Get suffix
                suffix = self.suffixes[len(triples) - 1 - num]
                if suffix is not None:
                    triple_text += f' {suffix}'
                # If not the biggest triple, and triple does not contain and, add and - e.g:
                # 1234 -> one thousand two hundred and eighty-four (no and required)
                # 1004 -> one thousand AND four (and required)
                if (num != 0) & ('and' not in triple_text) & ('hundred' not in triple_text):
                    triple_text = 'and ' + triple_text

                answer.append(triple_text)

            answer = ' '.join(answer)
            print(number)
            print(answer)
            self.answer += len(answer.replace(' ', '').replace('-', ''))

    @staticmethod
    def pad_number(number):
        pad = len(str(number)) % 3
        if pad == 0:
            return str(number)
        else:
            return '0' * (3 - pad) + str(number)

    def generate_triple_text(self, triple):
        h, t, u = str(triple)

        answer = []

        # When there is a hundred - 200 -> two hundred
        if h != '0':
            answer.append(f'{self.generate_unit_text(h)} hundred')

        # When something follows a hundred - 230 -> two hundred and thirty
        if (h != '0') and ((t != '0') or (u != '0')):
            answer.append('and')

        # When there is a tens (inc teens) - 20 -> twenty
        if t != '0':
            ans_temp = self.generate_tens_text(t, u)
            # When there is a tens (excl teens) and a unit (hyphen!) - 34 -> thirty-four
            if (t != '1') & (u != '0'):
                answer.append(f'{ans_temp}-{self.generate_unit_text(u)}')
            else:
                answer.append(ans_temp)

        elif u != '0':
            answer.append(self.generate_unit_text(u))

        return ' '.join(answer)

    @staticmethod
    def generate_unit_text(unit):
        if unit == '1':
            return 'one'
        elif unit == '2':
            return 'two'
        elif unit == '3':
            return 'three'
        elif unit == '4':
            return 'four'
        elif unit == '5':
            return 'five'
        elif unit == '6':
            return 'six'
        elif unit == '7':
            return 'seven'
        elif unit == '8':
            return 'eight'
        elif unit == '9':
            return 'nine'
        elif unit == '0':
            return ''

    def generate_tens_text(self, ten, unit):
        if ten == '1':
            return self.generate_teens_text(unit)
        elif ten == '2':
            return 'twenty'
        elif ten == '3':
            return 'thirty'
        elif ten == '4':
            return 'forty'
        elif ten == '5':
            return 'fifty'
        elif ten == '6':
            return 'sixty'
        elif ten == '7':
            return 'seventy'
        elif ten == '8':
            return 'eighty'
        elif ten == '9':
            return 'ninety'
        elif ten == '0':
            return ''

    @staticmethod
    def generate_teens_text(unit):
        if unit == '1':
            return 'eleven'
        elif unit == '2':
            return 'twelve'
        elif unit == '3':
            return 'thirteen'
        elif unit == '4':
            return 'fourteen'
        elif unit == '5':
            return 'fifteen'
        elif unit == '6':
            return 'sixteen'
        elif unit == '7':
            return 'seventeen'
        elif unit == '8':
            return 'eighteen'
        elif unit == '9':
            return 'nineteen'
        elif unit == '0':
            return 'ten'

if __name__ == '__main__':
    limit = 1000

    NumberLetterCounts(limit)
