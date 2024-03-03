__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Array Rank:

Given an array of distinct integers, replace each array element by its corresponding rank in the array.

The minimum array element has the rank 1; the second minimum element has a rank of 2, and so on…

Example:
    Input:  { 10, 8, 15, 12, 6, 20, 1 }
    Output: { 4, 3, 6, 5, 2, 7, 1 } 

Started: Mar 03, 2024 @ 4:35am ET
Intervals: 1
Ended: Marc 03, 2024 @ 5:05am ET
"""
from sys import argv

def rank_array(array: list) -> list:
    rank = 1
    indices = [array.index(x) for x in array]
    array_map = dict(zip(array, indices)) 
    

    for key in sorted(array_map.keys()):
        array[array_map.get(key)] = rank
        rank += 1
    
    print(array)
    


if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 10,8,15,12,6,20,1

    rank_array(array)