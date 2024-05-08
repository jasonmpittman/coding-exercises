__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Remove Smallest:
Create a function that takes an array of integers and removes the smallest value.

Examples
    removeSmallest([1, 2, 3, 4, 5] ) ➞ [2, 3, 4, 5]
    removeSmallest([5, 3, 2, 1, 4]) ➞ [5, 3, 2, 4]
    removeSmallest([2, 2, 1, 2, 1]) ➞ [2, 2, 2, 1]

Notes
    Don't change the order of the left over items.
    If you get an empty array, return an empty array: [] ➞ []
    If there are multiple items with the same value, remove item with lower index (3rd example).

Started: May 08, 2024 @ 5:55am ET
Intervals: 1
Ended: May 08, 2024 @ 6:06am ET    
"""
from sys import argv

def remove_smallest(array: list) -> list:
    """ iterates through array and removes smallest value """

    current = array[0]

    for i in range(1, len(array) - 1):
        if array[i] < current:
            current = array[i]

    array.remove(current)
    return array




if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 1,2,3,4,5 # 5,3,2,1,4 # 2,2,1,2,1
    
    smallest_removed = remove_smallest(array)
    print(smallest_removed)

