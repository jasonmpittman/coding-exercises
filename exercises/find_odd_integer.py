__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Find Odd Integer:

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
Examples

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

Started: May 18, 2024 @ 5:40am ET
Intervals: 1
Ended: May 18, 2024 @ 5:51am
"""
from sys import argv

def find_odd_integer(array: list) -> int:
    #odd_integer = {}

    # find the most occuring number in array
    #for number in array:
    #    odd_integer[number] = array.count(number)

    #return max(odd_integer)

    for number in array:
        if array.count(number) % 2 != 0:
            return number

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))

    odd_integer = find_odd_integer(array)
    print(odd_integer)