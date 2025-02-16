import utils.utils as utils
import numpy as np

class LongestCollatz:

    def __init__(self, limit):
        self.limit = int(limit)

        self.collatz_candidates = None
        self.collatz_map = {1: [1]}
        self.answer = 0

        self.get_answer()

    def get_answer(self):
        self.get_collatz_candidates()
        self.analyse_candidates()
        self.answer = sorted(self.collatz_map, key=lambda x: len(self.collatz_map[x]), reverse=True)[0]
        print(self.answer)
        print(f'chain length: {len(self.collatz_map[self.answer])}')

    def get_collatz_candidates(self):
        self.collatz_candidates = np.ones(self.limit + 1, dtype=np.bool)
        self.collatz_candidates[0] = False
        self.collatz_candidates[1] = False

    def analyse_candidates(self):
        for candidate in range(len(self.collatz_candidates)):
            if candidate in [0, 1]:
                continue
            else:
                self.generate_collatz_sequence(candidate)

    def generate_collatz_sequence(self, candidate):
            # to_check should be false where a sequence has already been saved
            to_check = self.collatz_candidates[candidate]
            if ~to_check:
                return

            sequence = [candidate]

            while candidate != 1:
                candidate = utils.collatz_next_number(candidate)

                candidate_map = self.collatz_map.get(candidate, None)
                # Case when collatz sequence for candidate is not mapped
                if candidate_map is None:
                    sequence.append(candidate)

                # Case when collatz sequence for candidate is mapped
                else:
                    full_sequence = sequence + candidate_map

                    # Reverse through the sequence of unmapped candidates, filling maps where required
                    for number in sequence[::-1]:
                        if self.collatz_map.get(number, True):
                            # Find index in sequence, then take from that index onwards from full_sequence
                            self.collatz_map[number] = full_sequence[sequence.index(number):]
                            # If number is in candidate list, set as false to avoid future runs
                            if number <= self.limit:
                                self.collatz_candidates[number] = False
                        else:
                            continue

                    # Once sequence has been mapped, break out of while loop
                    break

if __name__ == '__main__':
    limit = 1e6
    LongestCollatz(limit)
