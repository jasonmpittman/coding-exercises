__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Sum Numbers:
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Examples (a, b) --> output (explanation)
    (1, 0) --> 1 (1 + 0 = 1)
    (1, 2) --> 3 (1 + 2 = 3)
    (0, 1) --> 1 (0 + 1 = 1)
    (1, 1) --> 1 (1 since both are same)
    (-1, 0) --> -1 (-1 + 0 = -1)
    (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

Started: June 07, 2024 @ 6:30am ET
Intervals: 1
Ended: June 07, 2024 @ 6:34am ET
"""
from sys import argv

def sum_numbers(a: int, b: int) -> int:
    """ Returns sum of numbers between a and b, inclusive"""
    number = sum([x for x in range(a, b + 1)])
    print(number)

if __name__ == "__main__":
    a, b = int(argv[1]), int(argv[2])

    result = sum_numbers(a, b)
    