__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Zero Sum: 
Given an integer array, check if it contains a contiguous subarray having zero-sum.

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: True
Explanation: The subarrays with zero-sum are

[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Input : [4, -7, 1, -2, -1]
Output: False

Started: April 25, 2024 @ 6:25am ET
Intervals: 1
Ended: April 25, 2024 @ 6:42am ET
"""
from sys import argv

def find_subarrays(array: list) -> list:
    subarrays = []

    for i in range(len(array)):
        values = []
        values.append(array[i])
        
        for j in range(i + 1, len(array)):
            values.append(array[j])
        
            if sum(values) == 0:
                subarrays.append(values)  
                break

    return subarrays


if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 3,4,-7,3,1,3,1,-4,-2,-2
    subarrays = find_subarrays(array)

    for subarray in subarrays:
        print(subarray)
