__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Binary Search:
Given a sorted array of n integers and a target value, determine if the target exists in the array in logarithmic time using the binary search algorithm. If target exists in the array, print the index of it.

Examples:
    Input:   nums[] = [2, 3, 5, 7, 9] target = 7  
    Output: Element found at index 3    

    Input:   nums[] = [1, 4, 5, 8, 9] target = 2  
    Output: Element not found

Started: Mar 07, 2024 @ 6:00am ET
Intervals: 1
Ended: Marc 07, 2024 @ 6:21am ET
"""
from sys import argv

def search_binary(array: list, n: str, start: int, end: int) -> int:
    #start is left, end is right
    mid = (start + end) // 2
    

    if n == array[mid]:
        return mid
        
    elif n < array[mid]:
        search_binary(array, n, start, mid -1) 
        
    else: #n > array[mid]:
        search_binary(array, n, mid + 1, end)
    

if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 2,3,5,7,9
    n = int(argv[2]) # 7

    index = search_binary(array, n, 0, len(array) - 1)
    print(index)