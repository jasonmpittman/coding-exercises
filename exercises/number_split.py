__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Number Split:

Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.

Examples:

    number_split(4) ➞ [2, 2]
    number_split(10) ➞ [5, 5]
    number_split(11) ➞ [5, 6]
    number_split(-9) ➞ [-5, -4]


Started: Dec 29, 2023 @ 6:00am ET
Intervals: 1
Ended: Dec 29, 2023 @ 6:10am ET
"""

from sys import argv


def split_number(n):
    numbers = []

    q = n // 2
    numbers.append(q)
    
    if n % 2 != 0:
        numbers.append(numbers[0] + 1)
    else:
        numbers.append(q)

    if n < 0:
        numbers.sort(reverse=True)

    return numbers

if __name__ == '__main__':
    n = int(argv[1])
    
    print(split_number(n))