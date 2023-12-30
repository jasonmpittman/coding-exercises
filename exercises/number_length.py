__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Number Length:

Create a function that takes a number num and returns its length.

Examples:
    number_length(10) ➞ 2
    number_length(5000) ➞ 4
    number_length(0) ➞ 1


Started: Dec 30, 2023 @ 5:45am ET
Intervals: 1
Ended: Dec 30, 2023 @ 5:48am ET
"""
from sys import argv

def get_number_length(number: str) -> str:
    length = 0

    for digit in number:
        length += 1

    return length


if __name__ == '__main__':
    number = argv[1]

    print(get_number_length(number))
