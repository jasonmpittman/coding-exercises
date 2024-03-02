__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Array Depth:
Given an array, write a function to calculate it's depth. Assume that a normal array has a depth of 1.

Examples:
    depth([1, 2, 3, 4]) ➞ 1

    depth([1, [2, 3, 4]]) ➞ 2

    depth([1, [2, [3, 4]]]) ➞ 3

    depth([1, [2, [3, [4]]]]) ➞ 4

Started: Mar 02, 2024 @ 5:10am ET
Intervals: 1
Ended: Marc 02, 2024 @ 5:40am ET
"""
from collections import Counter

# this works but only with the +1 after the return
def calculate_depth(array: list) -> int:  
    
    depth = sum([1 + calculate_depth(i) for i in array if isinstance(i, list)])

    return depth

# TODO: this is off
def compute_depth(array: list) -> int:
    depth = Counter(map(len, array))
    s = 0
    print(depth)

    for k,v in depth.items():
        s += int(k) # do we want k or v here?
    
    print(s)

# this only works with string lists because of compute_depth
if __name__ == "__main__":
    array = ['1', ['2', '3', '4']] #['1', ['2', ['3', ['4']]]] #['1', ['2', '3', '4']] #[1, 2, 3, 4]

    depth = calculate_depth(array)
    print(depth + 1)

    compute_depth(array)