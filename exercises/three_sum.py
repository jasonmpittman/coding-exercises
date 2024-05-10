__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Three Sum:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Started: April 29, 2024 @ 7:15am ET
Intervals: 1
Ended: April 29, 2024 @ 7:45am ET
"""
from sys import argv

# TODO: implement non-contiguous search
def sum_three(nums: int, contiguous=True) -> list:
    sums = []
    i, j, k = 0, 1, 2
    length = len(nums)

    if contiguous is True:
        for _ in range(length - 2):
            # make sure i != j, i != k, and j != k
            if nums[i] == nums[j] or nums[i] == nums[k] or nums[j] == nums[k]:
                return sums
            elif (nums[i] + nums[j] + nums[k]) == 0:
                triplet = [nums[i], nums[j], nums[k]]
                sums.append(triplet)

            i += 1
            j += 1
            k += 1
        
        return sums
    
    # for each i, search for j and k across rest of nums 
    if contiguous is False:
        pass


if __name__ == "__main__":
    nums = list(map(int, argv[1].split(',')))

    print(sum_three(nums))