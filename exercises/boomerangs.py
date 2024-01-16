__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Boomerangs:
A boomerang is a V-shaped sequence that is either upright or upside down. Specifically, a boomerang can be defined as: sub-array of length 3, with the first and last digits being the same and the middle digit being different.

Examples:

[3, 7, 3, 2, 1, 5, 1, 2, 2, -2, 2]
// 3 boomerangs in this sequence:  [3, 7, 3], [1, 5, 1], [2, -2, 2]

[1, 7, 1, 7, 1, 7, 1]
// 5 boomerangs (from left to right): [1, 7, 1], [7, 1, 7], [1, 7, 1], [7, 1, 7], and [1, 7, 1]

    countBoomerangs([9, 5, 9, 5, 1, 1, 1]) ➞ 2
    countBoomerangs([5, 6, 6, 7, 6, 3, 9]) ➞ 1
    countBoomerangs([4, 4, 4, 9, 9, 9, 9]) ➞ 0

Inputs:
    3,7,3,2,1,5,1,2,2,-2,2 -> 3
    1,7,1,7,1,7,1 -> 5
    4,4,4,9,9,9,9 -> 0

Started: Jan 13, 2024 @ 6:30am ET
Intervals: 1
Ended: Jan 13, 2024 @ 6:46am ET
"""
from sys import argv

def count_boomerangs(boomerangs: list) -> int:
    count = 0
    length = len(boomerangs)
    left = 0
    right = 2

    while right < length:
        if boomerangs[left] == boomerangs[right] and boomerangs[left] != boomerangs[left + 1]:
            count += 1

        left += 1
        right += 1

    print(count)

if __name__ == '__main__':
    boomerangs = argv[1].split(',')

    count_boomerangs(boomerangs)