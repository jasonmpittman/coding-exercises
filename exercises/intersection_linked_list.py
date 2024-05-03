__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Intersection Linked List:
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Examples:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'

    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'

Started: May 03, 2024 @ 3:45am ET
Intervals: 1
Ended: May 03, 2024 @ 4:15am ET
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find_intersection(headA: ListNode, headB: ListNode) -> ListNode:
    a, b = headA, headB

    while (a != b):
        a = headB if not a else a.next
        b = headA if not b else b.next
    
    return a

if __name__ == "__main__":
    a = [4,1,8,4,5]
    b = [5,6,1,8,4,5]
    headA = ListNode(a[0])
    listA = headA
    headB = ListNode(b[0])
    listB = headB
    
    for _ in a[1:]:
        listA.next = ListNode(_)
        listA = listA.next

    for _ in b[1:]:
        listB.next = ListNode(_)
        listB = listB.next

    
