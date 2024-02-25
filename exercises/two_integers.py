__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Two Integers:

You are given an array of n integers, and your task is to find two values (at distinct positions) whose sum is x.

Example:

    Input:
    4 8
    2 7 5 1

    Output:
    2 4

Started: Feb 25, 2024 @ 6:50am ET
Intervals: 1
Ended: Feb 25, 2024 @ 7:15am ET
"""
from sys import argv

# TODO: need to handle no sum
def sum_two_integers(length: int, target_sum: int, numbers: list):
    x, y = 0, 0
    
    for i in range(length):
        y = numbers[i]
        for j in range(length):
            x = numbers[j]
            if x + y == target_sum:
                break

    print("Indices are: ", numbers.index(x) + 1, numbers.index(y) + 1) # +1 to convert to nonzero indexing


if __name__ == "__main__":
    length = int(argv[1])
    target_sum = int(argv[2])
    numbers = list(map(int, argv[3].split(','))) # 2,7,5,1

    sum_two_integers(length, target_sum, numbers)