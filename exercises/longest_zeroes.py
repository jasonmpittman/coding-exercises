__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Longest Zeroes:
Write a function that returns the longest sequence of consecutive zeroes in a binary string.

Examples
    longestZero("01100001011000") ➞ "0000"
    longestZero("100100100") ➞ "00"
    longestZero("11111") ➞ ""

Started: April 15, 2024 @ 2:50pm ET
Intervals: 1
Ended: April 13, 2024 @ 3:14pm ET
"""
from sys import argv
import re


def find_longest_zeroes(binary_string: str) -> str:
    longest_zeroes = ''

    pattern = re.compile(r'[0]+')
    matches = re.findall(pattern, binary_string)

    for match in matches:
        if len(match) > len(longest_zeroes):
            longest_zeroes = match

    return longest_zeroes

if __name__ == "__main__":
    binary_string = argv[1]

    longest = find_longest_zeroes(binary_string)
    print(longest)