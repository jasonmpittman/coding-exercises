#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Pancake Sort: https://old.reddit.com/r/dailyprogrammer/comments/np3sio/20210531_challenge_392_intermediate_pancake_sort/

Implement the flipfront function. Given an array of integers and a number n between 2 and the length of the array (inclusive), return the array with the order of the first n elements reversed.

flipfront([0, 1, 2, 3, 4], 2) => [1, 0, 2, 3, 4]
flipfront([0, 1, 2, 3, 4], 3) => [2, 1, 0, 3, 4]
flipfront([0, 1, 2, 3, 4], 5) => [4, 3, 2, 1, 0]
flipfront([1, 2, 2, 2], 3) => [2, 2, 1, 2]

Started: Dec 10, 2023 @ 3:15am ET
Intervals: 1
Ended: Dec 10, 2023 @ 3:30am ET

"""
from sys import argv

def flip_front(array, n):
    #print(array)

    # get slice of array based on n
    front = array[:n]
    for i in range(len(front)):
        array[i] = front[-1]
        front.pop(-1)
    
    return array

    
if __name__ == '__main__':
    # 01234,2 01234,3 01234,5
    array, n = argv[1].split(',')
    flip_front(list(array), int(n))