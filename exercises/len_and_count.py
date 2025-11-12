__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Implement length to count the number of nodes in a linked list.

    length(null) => 0
    length(1 -> 2 -> 3 -> null) => 3

Implement Count() to count the occurrences of an integer in a linked list.

    count(null, 1) => 0
    count(1 -> 2 -> 3 -> null, 1) => 1
    count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4


Start: 4:45am
End: 05:00am
Cycles: 1
"""
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
    
    #   custom method
    def length(self) -> int:
        """ return count of all nodes in the linked list """
        length = 0
        current = self.head

        while current:
            length += 1
            current = current.next
        
        return length

    #   custom method
    def count(self, n: int) -> int:
        """ return count of an integer n in linked list """
        count = 0
        current = self.head

        while current:
            if current.data == n:
                count += 1
            
            current = current.next
        
        return count

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    n = 3

    linked_list.display()
    print(f'Length is: {linked_list.length()}')
    print(f'Count of {n} is: {linked_list.count(n)}')