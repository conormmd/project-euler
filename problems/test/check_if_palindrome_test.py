import pandas as pd
import utils.utils as utils
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        test_data = pd.DataFrame(
            columns=['candidate', 'output'],
            data = [
                [1, True],
                [22, True],
                [13, False],
                ['abcCBA', False],
                ['wowawewawow', True],
                ['palindrome', False],
                ['a man a plan a canal panama', False],
                ['amanaplanacanalpanama', True],
            ]
        )

        for idx, row in test_data.iterrows():
            output = utils.check_if_palindrome(row['candidate'])
            expected_output = row['output']
            self.assertEqual(output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
