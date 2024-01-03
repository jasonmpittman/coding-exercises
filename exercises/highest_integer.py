__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Highest Integer:

Create a function that finds the highest integer in the list using recursion.

Examples:
    find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99
    find_highest([0, 12, 4, 87]) ➞ 87
    find_highest([8]) ➞ 8

Started: Jan 03, 2024 @ 6:30am ET
Intervals: 1
Ended: Jan 03, 2024 @ 7:00am ET
"""
from sys import argv


if __name__ == '__main__':
    integers = argv[1]