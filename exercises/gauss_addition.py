__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Gauss Addition: https://edabit.com/challenge/BE2FQ3xwFAC5ZbgPY

Create a function that adds all the numbers together from 1 to n or, if two numbers are given: n to m. The input can be in any order.

Example:
    Gauss({ 100 }) ➞ 5050 // From the video
    Gauss({ 5001, 7000 }) ➞ 12001000 // Also ^^
    Gauss({ 1975, 165 }) ➞ 1937770

Started: Feb 11, 2024 @ 11:00am ET
Intervals: 1
Ended: Feb 11, 2024 @ 11:30am ET
"""
from sys import argv

# formula
# add first + last n ... 1 + 100 = 101
# cut input in half = 1...100 is a 50-51 or 100 // 2 is 50 and 101 - 50 is 51
# l x h -> total or 50 x 101 = 5050

# TODO: correct for 1...100 but not for others. need to troubleshoot
def add(n, m) -> int:
    first_number = n
    last_number = m
    sum_number = first_number + last_number

    dividend = sum_number // 2
    gauss_number = dividend * sum_number

    return gauss_number

if __name__ == '__main__':
    n = int(argv[1])
    m = int(argv[2])
    result = add(n, m)  

    print(result)