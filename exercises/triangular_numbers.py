__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Triangular Numbers:
Write a function that returns the number of dots when given its corresponding triangle number of the sequence.

Examples:
    triangle(1) ➞ 1
    triangle(6) ➞ 21
    triangle(215) ➞ 23220

Started: Jan 07, 2024 @ 7:00am ET
Intervals: 1
Ended: Jan 07, 2024 @ 7:30am ET
"""
from sys import argv

def build_triangular(n: int):
    dots = n

    for i in range(1, n):
        dots += n - i

    return dots

if __name__ == '__main__':
    n = int(argv[1])

    print(build_triangular(n))