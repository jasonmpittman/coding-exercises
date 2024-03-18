__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Exponential Search:

Given a sorted array of n integers and a target value, determine if the target exists in the array or not in logarithmic time. If the target exists in the array, return the index of it.

Examples:
    Input: A[] = [2, 3, 5, 7, 9] target = 7  
    Output: Element found at index 3    
    
    Input: A[] = [1, 4, 5, 8, 9] target = 2  
    Output: Element not found 

Started: Mar 17, 2024 @ 4:45am ET
Intervals: 1
Ended: March 17, 2024 @ 5:25am ET
"""
from sys import argv

def search(array: list, target: int) -> int:
    index = 1
    length = len(array)

    if length == 0:
        return -1
    
    while index < length and array[index] < target:
        index *= 2

    left = index // 2
    right = min(index, length - 1)

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1


if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 2,3,4,10,40 10
    target = int(argv[2])

    result = search(array, target)
    print(result)