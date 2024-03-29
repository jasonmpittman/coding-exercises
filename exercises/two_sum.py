__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Two Sum:
Given an unsorted integer array, find a pair with the given sum in it.

• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()

Started: Mar 27, 2024 @ 4:40am ET
Intervals: 1
Ended: March 27, 2024 @ 5:10am ET
"""
from sys import argv
import math

    
def find_sum(array: list, target: int) -> tuple:

    if len(array) < 2:
        return tuple()

    # compute the complementary of target and number in array and if in array return number & complementary
    # greedy match
    for i, number in enumerate(array[:-1]):
        complementary = target - number # f.ex: 10 - 8 = c
        if complementary in array[i + 1:]:
            return number, complementary
        
    return tuple()

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    target = int(argv[2])

    result = find_sum(array, target)
    print(result)