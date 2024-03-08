__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Unique Sort: 
Given an array of numbers, write a function that returns an array that...

    Has all duplicate elements removed.
    Is sorted from least to greatest value.

Examples:
    uniqueSort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
    uniqueSort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
    uniqueSort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]   


Started: Mar 08, 2024 @ 5:10am ET
Intervals: 1
Ended: Marc 08, 2024 @ 5:20am ET
"""
from sys import argv

# the 'easy' way
def sort_unique(array: list) -> list:
    return set(sorted(array))



if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 1,2,4,3 # 1,4,4,4,4,4,3,2,1,2

    print(sort_unique(array))