__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Remove Nth:
Given the head of a linked list, remove the nth node from the list and return its head.

    Example:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,4,5]

    Input: head = [1], n = 1
    Output: []

    Input: head = [1,2], n = 1
    Output: [1]

Started: April 09, 2024 @ 5:10am ET
Intervals: 1
Ended: April 09, 2024 @ 5:40am ET
"""
from sys import argv
import LinkedList
from collections import deque

if __name__ == "__main__":
    if argv[1] == 'default':
        array = argv[2].split(',')
        n = int(argv[3])

        llist = LinkedList.LinkedList()
        for a in array:
            llist.insertAtEnd(a)
        
        llist.printLL()
        llist.remove_at_index(n)
        llist.printLL()
    # TODO: del works but not with 0 indexing
    elif argv[1] == 'deque':
        llist = deque(argv[2])
        n = int(argv[3])
        del llist[n]
        print(llist)