__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


""" Merge Sort:

    Divide the unsorted array into n subarrays, each of size 1 (an array of size 1 is considered sorted).
    Repeatedly merge subarrays to produce new sorted subarrays until only 1 subarray is left, which would be our sorted array.


Started: June 14, 2024 @ 10:20am ET
Intervals: 1
Ended: June 14, 2024 @ 10:50am ET
"""


def merge_sort(array: list) -> list:
    """Returns sorted array"""

    divided_array = [[x] for x in array]
    

if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]

    sorted_array = merge_sort(array)
    print(sorted_array)