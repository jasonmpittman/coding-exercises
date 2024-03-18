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





if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))