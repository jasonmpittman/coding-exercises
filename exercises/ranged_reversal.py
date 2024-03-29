__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Ranged Reversal:
Write a function that reverses the subarray between the start and end index (inclusive). The rest of the array should be kept the same.

Examples:
    rangedReversal([1, 2, 3, 4, 5, 6], 1, 3) ➞ [1, 4, 3, 2, 5, 6]
    rangedReversal([1, 2, 3, 4, 5, 6], 0, 4) ➞ [5, 4, 3, 2, 1, 6]
    rangedReversal([9, 8, 7, 4], 0, 0) ➞ [9, 8, 7, 4]

Started: Mar 22, 2024 @ 6:00am ET
Intervals: 1
Ended: March 22, 2024 @ 6:12am ET
"""
from sys import argv


def reverse_array(array: list, start: int, stop:int) -> list:

    array[start: stop + 1] = array[stop : start - 1: -1]

    return array

if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 1,2,3,4,5,6 1 3
    start = int(argv[2])
    stop = int(argv[3])

    reversed_array = reverse_array(array, start, stop)
    print(reversed_array)