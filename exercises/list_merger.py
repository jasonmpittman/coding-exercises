#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""List Merger

Write a function that merges two sorted lists (arrays) into one new sorted list. The two input lists will be sorted in ascending order. The merged list should also be sorted in ascending order. You should not use any built-in sort methods to achieve this; instead, manually merge the two lists.

Test cases:

    mergeSortedLists([1, 3, 5], [2, 4, 6]) should return [1, 2, 3, 4, 5, 6].
    mergeSortedLists([1, 2, 3], []) should return [1, 2, 3] (one list is empty).
    mergeSortedLists([], [4, 5, 6]) should return [4, 5, 6] (the other list is empty).
    mergeSortedLists([1, 1, 1], [2, 2, 2]) should return [1, 1, 1, 2, 2, 2] (handling duplicates).

    1, 3, 5
    2, 4, 6

Started: Nov 30, 2023 @ 6:00am ET
Intervals: 1
Ended: Nov 30, 2023 @ 6:30am ET   

"""
# added for unittest challenge 12/15/23
def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list

# code below here was its own challenge on 11/30/23
def merge_lists(lists):
    return lists[0] + lists[1]

# insertion sort    
def sort_lists(merged_list):
    sorted_list = []
    
    for i in range(1, len(merged_list)):
        key = merged_list[i] # set to b in a <> b
        j = i - 1 # set to a in a <> b

        while j >= 0 and key < merged_list[j]: 
            merged_list[j + 1] = merged_list[j]
            j -= 1
        
        merged_list[j + 1] = key

    return merged_list


# TODO: how to take list of lists from argv
if __name__ == '__main__':
    lists = [[1, 1, 1], [2, 2, 2]]

    merged_list = merge_lists(lists)
    
    sorted_list = sort_lists(merged_list)
    print(sorted_list)