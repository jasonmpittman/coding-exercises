__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Kth Largest: 
Given an integer array, find k'th largest element in the array where k is a positive integer less than or equal to the length of array.

Input : [7, 4, 6, 3, 9, 1], k = 2
Output: 7
Explanation: The 2nd largest array element is 7

Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 4
Output: 4
Explanation: The 4th largest array element is 4

Started: April 26, 2024 @ 3:20am ET
Intervals: 1
Ended: April 26, 2024 @ 3:34am ET
"""
from sys import argv

def find_kth_largest(array: list, k) -> int:
    sorted_array = sorted(array)
    
    return sorted_array[-2]


if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    k = int(argv[2])
    
    kth_largest = find_kth_largest(array, k) # 7,4,6,3,9,1 2
    print(kth_largest)


