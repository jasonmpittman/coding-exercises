__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Nth Sum:
Given an array of numbers and a positive value for n, return the sum of every nth number in the array.

Examples

    sumEveryNth([4, 8, 6, 6, 7, 9, 3], 1) ➞ 43
    // 4+8+6+6+7+9+3 = 43

    sumEveryNth([7, 3, 10, 4, 5, 8, 4, 9, 6, 9, 10, 1, 4], 4) ➞ 14
    // 4+9+1 = 14

    sumEveryNth([10, 6, 5, 4, 5, 2, 3, 3, 8, 10, 7, 2], 8) ➞ 3
    // 3

    sumEveryNth([6, 8, 9, 4, 6, 4, 7, 1, 5, 6, 10, 2], 13) ➞ 0
    // only 12 numbers in array

Started: Mar 28, 2024 @ 7:25am ET
Intervals: 1
Ended: March 28, 2024 @ 7:45am ET
"""
from sys import argv


def sum_nth(array: list, n: int) -> int:
    nth = 0

    for i in range(n - 1, len(array), n):
        nth += array[i]
    
    return nth

if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 4,8,6,6,7,9,3 1  # 7,3,10,4,5,8,4,9,6,9,10,1 4
    n = int(argv[2])

    print(sum_nth(array, n))