__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Start: 4:44am 
End: 4:49am
"""

def main(nums: list, target: int) -> list:
    indices = []

    for i in range(len(nums) - 1):
        if nums[i] + nums[i + 1] == target:
            indices.extend([i, i + 1])
            break
    
    return indices

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6

    indices = main(nums, target)
    print(indices)