__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" List Multiples:
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.

Examples:
    list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
    list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

Started: Dec 31, 2023 @ 6:05am ET
Intervals: 1
Ended: Dec 31, 2023 @ 6:12am ET
"""

from sys import argv

def list_mupltiples(n, m):
    multiples = [n]
    base = n

    for _ in range(m - 1):
        n = n + base
        multiples.append(n)

    return multiples


if __name__ == '__main__':
    n,m = argv[1].split(',')

    print(list_mupltiples(int(n), int(m)))
