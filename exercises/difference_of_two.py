__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Difference of Two:
The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

The result array should be sorted in ascending order of values.

Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

Examples
    [1, 2, 3, 4]  should return [[1, 3], [2, 4]]
    [4, 1, 2, 3]  should also return [[1, 3], [2, 4]]
    [1, 23, 3, 4, 7] should return [[1, 3]]
    [4, 3, 1, 5, 6] should return [[1, 3], [3, 5], [4, 6]]

Started: May 12, 2024 @ 7:00am ET
Intervals: 1
Ended: May 12, 2024 @ 7:12am
"""
from sys import argv

def is_difference(a: int, b: int) -> bool:
    if a - b == 2:
        return True
    else:
        return False

def sort_by_differences(array: list) -> list:
    sorted_array = []

    for i in range(len(array)):
        for j in range(len(array)):
            if is_difference(array[i], array[j]):
                sorted_array.append(sorted((array[i], array[j])))

    return sorted_array

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    
    sorted_array = sort_by_differences(array)
    print(sorted_array)