__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Pair Sum:

Given an unsorted integer array, find a pair with the given sum in it.

Examples:
    Input:   nums = [8, 7, 2, 5, 3, 1] target = 10  
    Output:   Pair found (8, 2) or Pair found (7, 3)

    Input:   nums = [5, 2, 6, 8, 1, 9] target = 12  
    Output: Pair not found 

Started: Feb 16, 2024 @ 5:45am ET
Intervals: 1
Ended: Feb 16, 2024 @ 6:01am ET
"""
from sys import argv

def brute_force(numbers: list, target: int) -> int:

    for i in range(len(numbers) - 1):
        
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(numbers[i], numbers[j])  
            

if __name__ == '__main__':
    numbers = [int(x) for x in argv[1].split(',')] # 8,7,2,5,3,1
    target = int(argv[2])

    brute_force(numbers, target)