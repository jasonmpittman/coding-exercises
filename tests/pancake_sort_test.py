#!/usr/bin/env python

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

class PancakeSortTest(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()

