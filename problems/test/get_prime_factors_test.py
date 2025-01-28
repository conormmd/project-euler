import pandas as pd
import utils.utils as utils
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        test_data = pd.DataFrame(
            columns=['number', 'output'],
            data = [
                [12, [2, 2, 3]],
                [7, [7]],
                [100, [2, 2, 5, 5]],
                [69, [3, 23]],
                [1070, [2, 5, 107]],
            ]
        )

        for idx, row in test_data.iterrows():
            output = utils.get_prime_factors(row['number'])
            expected_output = row['output']
            self.assertEqual(output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
