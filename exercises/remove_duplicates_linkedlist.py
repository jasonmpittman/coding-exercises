__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Remove Duplicates:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Examples:
    Input: head = [1,1,2]
    Output: [1,2]

    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

Started: April 28, 2024 @ 5:00am ET
Intervals: 1
Ended: April 28, 2024 @ 5:30am ET
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicate(head: ListNode) -> ListNode:
    linked_list = head

    if head is None:
        return None
            
    while linked_list is not None and linked_list.next is not None:
        if linked_list.val == linked_list.next.val:
            linked_list.next == linked_list.next.next
        else:
            linked_list = linked_list.next
            
    return head

if __name__ == "__main__":
    nums = [1,1,2]
    head = ListNode(nums[0])
    current = head
    
    # Iterate over the remaining elements in nums and create nodes
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next

    print(remove_duplicate(head))