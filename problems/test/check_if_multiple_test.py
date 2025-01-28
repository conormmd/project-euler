import pandas as pd
import utils.utils as utils
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        test_data = pd.DataFrame(
            columns=['number', 'factor', 'output'],
            data = [
                [12, 5, False],
                [100, 10, True],
                [99, 9, True],
                [79, 43, False],
            ]
        )

        for idx, row in test_data.iterrows():
            output = utils.check_if_multiple(row['number'], row['factor'])
            expected_output = row['output']
            self.assertEqual(output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
