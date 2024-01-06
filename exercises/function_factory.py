__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Function Factory:

Create a function that takes a "base number" as an argument. This function should return another function which takes a new argument, and returns the sum of the "base number" and the new argument.

Examples:

    plusFive = makePlusFunction(5)
    plusFive(2) ➞ 7
    plusFive(-8) ➞ -3

    plusTen = makePlusFunction(10)
    plusTen(0) ➞ 10
    plusTen(188) ➞ 198
    plusFive(plusTen(0)) ➞ 15

    
Started: Jan 06, 2024 @ 2:10pm ET
Intervals: 1
Ended: Jan 06, 2024 @ 2:15pm ET
"""
from sys import argv

def make_function(n: int):
    
    def made_function(m: int):
        return n + m
    
    return made_function


if __name__ == '__main__':
    n, m = argv[1].split(',')

    made = make_function(int(n))
    sum = made(int(m))

    print(sum)