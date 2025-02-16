import pandas as pd
import utils.utils as utils
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        test_data = pd.DataFrame(
            columns=['number', 'output'],
            data = [
                [12, 6],
                [7, 22],
                [100, 50],
                [69, 208],
                [1070, 535],
                [999, 2998]
            ]
        )

        for idx, row in test_data.iterrows():
            output = utils.collatz_next_number(row['number'])
            expected_output = row['output']
            self.assertEqual(output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
