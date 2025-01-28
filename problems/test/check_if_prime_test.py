import pandas as pd
import utils.utils as utils
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        test_data = pd.DataFrame(
            columns=['number', 'output'],
            data = [
                [1, False],
                [2, True],
                [3, True],
                [4, False],
                [73, True],
                [75, False],
            ]
        )

        for idx, row in test_data.iterrows():
            output = utils.check_if_prime(row['number'])
            expected_output = row['output']
            self.assertEqual(output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
