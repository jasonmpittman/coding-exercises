__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Remove Marked:
Create a function that removes from a given array of integers all the values contained in a second array.

Examples (input -> output):
    * [1, 1, 2, 3, 1, 2, 3, 4], [1, 3] -> [2, 2, 4]
    * [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2] -> [5, 6, 7, 8]
    * [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3] -> [8, 7, 6, 5, 1]

# finished ahead of date due to vacation
Started: May 25, 2024 @ 6:00am ET
Intervals: 1
Ended: May 25, 2024 @ 6:30am ET
"""
from sys import argv

def remove_elements(array, to_remove):
    return [item for item in array if item not in to_remove]


if __name__ == '__main__':
    array = argv[1].split(',') # 1,1,2,3,1,1,2,3,4 1,3 # 8,2,7,2,3,4,6,5,4,4,1,2,3 2,4,3
    subarray = argv[2].split(',') 

    new_array = remove_elements(array, subarray)
    print(new_array)