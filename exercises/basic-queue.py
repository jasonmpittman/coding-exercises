
#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Basic Queue:
Write a class (or function, depending on your language of choice) that implements a queue using two stacks. The queue should support basic operations like enqueue (adding an element), dequeue (removing an element), and checking if the queue is empty.

Test Cases:
    Enqueue elements 1, 2, 3, then dequeue one element (should return 1).
    Enqueue elements 4, 5 after the above operation, then dequeue two elements (should return 2 and 3).

Started: Dec 09, 2023 @ 5:20am ET
Intervals: 1
Ended: Dec 09, 2023 @ 5:50am ET
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def get_size(self):
        """Return the size of the stack"""
        return self.size

    def is_empty(self):
        """Return True if the stack is empty"""
        if self.size == 0:
            return True
        else:
            return False

    def peek(self):
        """Get the top value in the stack"""
        if self.is_empty():
            raise Exception("Peeking an empty stack")
        
        return self.head.next.value


    def push(self, value):
        """Add a value to the stack LIFO"""
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        """Remove a value from the stack LIFO"""
        if self.is_empty():
            raise Exception("Popping an empty stack")
        
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1

        return remove.value
   


class Queue:

    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()


    def enqueue(self, value):
        self.enqueue_stack.push(value)

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        
        return self.dequeue_stack.pop()

    def is_empty(self):
        return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()

if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())

    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())