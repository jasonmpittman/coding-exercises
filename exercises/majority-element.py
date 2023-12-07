#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"



""" Majority Element:

Write a function that finds the majority element in an array of integers. The majority element is the element that appears more than n/2 times, where n is the size of the array. You may assume that the array is non-empty and the majority element always exists in the array.

Example Cases to Test:

    findMajorityElement([3, 3, 4, 2, 4, 4, 2, 4, 4]) should return 4.
    findMajorityElement([2, 2, 1, 1, 2, 2, 2]) should return 2.

Extensions (If you have extra time):

    Implement the function to handle cases where there might not be a majority element.
    Optimize the function for large arrays.

334244244

Started: Dec 07, 2023 @ 5:20am ET
Intervals: 1
Ended: Dec 07, 2023 @ 5:50am ET

"""

from sys import argv

def find_majority_element(array):
    """Initialize: Start with no candidate element and a count of 0.

    First Pass (Identifying a Candidate):
        Iterate through the array.
        If the count is zero, choose the current element as the candidate.
        If the current element is the same as the candidate, increment the count.
        Otherwise, decrement the count.
        At the end of this pass, if there is a majority element, it will be the candidate.

    Second Pass (Confirmation - Optional in this case):
        It's usually needed to confirm that the candidate is indeed the majority element.
        Iterate through the array and count the occurrences of the candidate.
        If the count is greater than n/2, return the candidate; otherwise, conclude there is no majority element."""
    
    pass





if __name__ == '__main__':
    elements = list(input('Enter the array: '))
    