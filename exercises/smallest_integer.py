__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Smallest Integer:
Given an array of integers your solution should find the smallest integer.

For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.

Started: Feb 25th, 2025 @ 06:10am ET
Intervals: 1
Ended: Feb 25th, 2025 @ 6:40am ET
"""
from heapq import heappop, heapify, heappush

def sort_heap(numbers: list) -> list:
    heapify(numbers)

    return numbers 

if __name__ == "__main__":
    numbers = [34, -345, -1, 100]

    heap = sort_heap(numbers)
    print(heap[0])