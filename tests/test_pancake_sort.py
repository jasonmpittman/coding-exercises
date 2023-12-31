__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


import unittest

try:
    from exercises import pancake_sort 
except ImportError as e:
    print(e)
# run from root as python3 -m unittest tests/test_pancake_sort.py

class PancakeSortTest(unittest.TestCase):
    #01234,2 01234,3 01234,5

    def test_pancake_two(self):
        self.assertEqual(pancake_sort.flip_front([0, 1, 2, 3, 4], 2), [1, 0, 2, 3, 4], 'The sort is incorrect')

    def test_pancake_three(self):
        self.assertEqual(pancake_sort.flip_front([0, 1, 2, 3, 4], 3), [2, 1, 0, 3, 4], 'The sort is incorrect')

    def test_pancake_five(self):
        self.assertEqual(pancake_sort.flip_front([0, 1, 2, 3, 4], 5), [4, 3, 2, 1, 0], 'The sort is incorrect')



if __name__ == '__main__':
    unittest.main()

