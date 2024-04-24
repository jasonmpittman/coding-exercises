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

Started: April 24, 2024 @ 5:50am ET
Intervals: 1
Ended: April 24, 2024 @ 6:01am ET
"""
from sys import argv

def find_paired_sum(array: list, target: int) -> tuple:
    sums = []

    # 8,2 and 2,8 are unqiue in this non-greedy version
    for number in array:
        for i in range(len(array)):
            if number + array[i] == target:
                pair = (number, array[i])
                sums.append(pair)

    print(sums)

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    target = int(argv[2])

    find_paired_sum(array, target) # 8,7,2,5,3 10