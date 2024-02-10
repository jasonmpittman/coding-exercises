__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" List Depth: 

Given an array, write a function to calculate it's depth. Assume that a normal array has a depth of 1.

Examples:
    depth([1, 2, 3, 4]) ➞ 1
    depth([1, [2, 3, 4]]) ➞ 2
    depth([1, [2, [3, 4]]]) ➞ 3
    depth([1, [2, [3, [4]]]]) ➞ 4

Started: Feb 10, 2024 @ 12:55pm ET
Intervals: 1
Ended: Feb 10, 2024 @ 1:06pm ET
"""

def compute_depth(my_list: list) -> int:

    if isinstance(my_list, list):
        if (len(my_list) == 0):
            depth = 1
        else:
            depth = 1 + max([compute_depth(l) for l in my_list])
    else:
        depth = 0

    return depth

if __name__ == '__main__':
    my_list = [1, [2, [3, [4]]]] # [1, [2, [3, 4]]] # [1, [2, 3, 4]] # [1, 2, 3, 4]
    print(compute_depth(my_list))