__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Least Larger:
Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Examples:
    leastLarger( [4, 1, 3, 5, 6], 0 )  =>  3
    leastLarger( [4, 1, 3, 5, 6], 4 )  => -1

Started: May 07, 2024 @ 5:50am ET
Intervals: 1
Ended: May 07, 2024 @ 5:59am ET
"""
from sys import argv

def find_least_larger(array: list, index: int) -> int:
    target = array[index]

    # sort array
    sorted_array = sorted(array)
    
    # find target index
    target_index = sorted_array.index(target)

    # return new index + 1 if new index is not last in array
    if target_index is not (len(sorted_array) - 1):
        return target_index + 1 
    else:
        return '-1'

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    index = int(argv[2])

    if len(array) == 0:
        print('-1')
    else:
        result = find_least_larger(array, index) # 4,1,3,5,6 0  4,1,3,5,6 4
        print(result)
