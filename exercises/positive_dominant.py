__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Positive Dominant:
An array is positive dominant if it contains strictly more unique positive values than unique negative values. Write a function that returns true if an array is positive dominant.

Examples:
    isPositiveDominant([1, 1, 1, 1, -3, -4]) ➞ false
    // There is only 1 unique positive value (1).
    // There are 2 unique negative values (-3, -4).

    isPositiveDominant([5, 99, 832, -3, -4]) ➞ true
    isPositiveDominant([5, 0]) ➞ true
    isPositiveDominant([0, -4, -1]) ➞ false

Started: Jan 14, 2024 @ 5:45am ET
Intervals: 1
Ended: Jan 14, 2024 @ 6:09am ET
"""
from sys import argv

def is_positive_dominant(numbers: list) -> bool:
    positive_count = 0
    negative_count = 0

    # we use len() to get the number of x after the conditional
    positive_count = len([x for x in numbers if x > 0])
    negative_count = len([x for x in numbers if x < 0])

    if positive_count > negative_count:
        return True
    else:
        return False

if __name__ == '__main__':
    numbers = argv[1].split(',')

    # we use list(map()) to cast str elements to integers
    result = is_positive_dominant(list(map(int,numbers))) #5,99,832,-3,-4 True
    print(result)