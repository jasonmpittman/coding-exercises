#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

import sys

"""Nonogram Row: https://old.reddit.com/r/dailyprogrammer/comments/o4uyzl/20210621_challenge_395_easy_nonogram_row/

Given a binary array of any length, return an array of positive integers that represent the lengths of the sets of consecutive 1's in the input array, in order from left to right.

Test input:
    nonogramrow([]) => []
    nonogramrow([0,0,0,0,0]) => []
    nonogramrow([1,1,1,1,1]) => [5]
    nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) => [5,4]
    nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) => [2,1,3]
    nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) => [2,1,3]
    nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) => [1,1,1,1,1,1,1,1]

Started: Nov 22, 2023 @ 7:00am ET
Intervals: 1
Ended: Nov 22, 2023 @ 7:30am ET

"""

def count_ones(nonogram):
    ones = nonogram.split('0')

    while ('' in ones):
        ones.remove('')
    
    while(',' in ones):
        ones.remove(',')

    return ones

# TODO: need to handle no argv
if __name__ == "__main__":
    nonogram = sys.argv[1]
    
    count = []
    ones = count_ones(nonogram)

    for i in ones:
        i = i.replace(',', "")
        count.append(len(i.strip()))

    print(count)