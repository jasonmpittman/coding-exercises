__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Strictly Increasing:
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

Example 1:
    Input: nums = [1,2,10,5,7]
    Output: true
    Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
    [1,2,5,7] is strictly increasing, so return true.

Example 2:
    Input: nums = [2,3,1,2]
    Output: false
    Explanation:
    [3,1,2] is the result of removing the element at index 0.
    [2,1,2] is the result of removing the element at index 1.
    [2,3,2] is the result of removing the element at index 2.
    [2,3,1] is the result of removing the element at index 3.
    No resulting array is strictly increasing, so return false.

Example 3:
    Input: nums = [1,1,1]
    Output: false
    Explanation: The result of removing any element is [1,1].
    [1,1] is not strictly increasing, so return false.


Started: May 02, 2024 @ 6:35am ET
Intervals: 1
Ended: May 02, 2024 @ 7:05am ET
"""
from sys import argv

def canBeIncreasing(nums):
    def isIncreasing(arr):
        for i in range(1, len(arr)):
            if arr[i - 1] >= arr[i]:
                return False
        return True
    
    for i in range(len(nums)):
        if isIncreasing(nums[:i] + nums[i+1:]):
            return True
    
    return False

if __name__ == "__main__":
    nums = list(map(int, argv[1].split(',')))

    result = canBeIncreasing(nums)
    print(result)