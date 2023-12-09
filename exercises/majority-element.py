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

Started: Dec 07, 2023 @ 5:20am ET
Intervals: 1
Ended: Dec 07, 2023 @ 5:50am ET

"""

from sys import argv

def find_majority(votes, n):
    majority = None
    majority_count = 0
    
    for vote in votes:
        if majority_count == 0:
            majority = vote
        if vote == majority:
            majority_count += 1
        else:
            majority_count -= 1
    
    return majority

def find_majority_element(elements, n):
    """Initialize: Start with no candidate element and a count of 0.

    First Step (Identifying a Candidate):
        Initialize a variable say i ,votes = 0, candidate =-1 
        Traverse through the array using for loop
        If votes = 0, choose the candidate = arr[i] , make votes=1.
        else if the current element is the same as the candidate increment votes
        else decrement votes.


    Second Step:
        Initialize a variable count =0 and increment count if it is the same as the candidate.
        If the count is >N/2, return the candidate.
        else return -1.
"""
    
    votes = 0
    candidate = -1

    for i in range(n):
        if votes == 0:
            votes = 1
            candidate = int(elements[i])
        else:
            if candidate == int(elements[i]):
                votes += 1
            else:
                votes -+ 1

    count = 0

    for i in range(n):
        if int(elements[i]) == candidate:
            count += 1

    if count > n // 2:
        return candidate
    else:
        return -1
    


# TODO: works for active list but not commented list
if __name__ == '__main__':
    elements = [2, 2, 1, 1, 2, 2, 2] #[ 1, 1, 1, 1, 2, 3, 4 ]
    #majority = find_majority_element(elements, len(elements))
    
    majority = find_majority(elements, len(elements))
    print(majority)