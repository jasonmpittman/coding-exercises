__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Least Common Multiple:
Given an array of integers, create a function that will find the smallest positive integer that is evenly divisible by all the members of the array. In other words, find the least common multiple (LCM).

Examples
    lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520
    lcm([5]) ➞ 5
    lcm([5, 7, 11]) ➞ 385
    lcm([5, 7, 11, 35, 55, 77]) ➞ 385

Started: Mar 17, 2024 @ 4:50am ET
Intervals: 1
Ended: March 17, 2024 @ 5:20am ET
"""
from sys import argv
from functools import reduce
import math


if __name__ == "__main__":
    numbers = list(map(int, argv[1].split(','))) # 1,2,3,4,5,6,7,8,9
    
    # using math package
    lcm = math.lcm(*numbers)
    print(lcm)

    # using math.gcd with reduce
    lcm = reduce(lambda a,b: a * b // math.gcd(a,b), numbers)
    print(lcm)