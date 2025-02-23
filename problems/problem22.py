import math
import numpy as np

class NamesScores:

    def __init__(self, names_raw):
        self.names = list()
        self.process_names(names_raw)

        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.answer = np.sum((idx + 1) * (ord(character) + 1 - ord('A')) for idx, name in enumerate(self.names) for character in name)
        print(self.answer)

    def process_names(self, names_raw):
        self.names = sorted(names_raw.replace('"', '').split(','))

if __name__ == '__main__':
    path = 'C:/Users/Conor/PycharmProjects/project-euler/problems/files/'
    filename = '0022_names.txt'

    with open(f'{path}{filename}', 'r') as file:
        names = file.read()

    NamesScores(names)
