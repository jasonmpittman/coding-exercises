#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Circular Buffer:

Write a class that implements a circular buffer. A circular buffer is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end. It should support operations like reading, writing, and overwriting when the buffer is full.

    Create a circular buffer with a capacity of 3.
    Write 3 elements and then write another one. If in overwrite mode, the buffer should overwrite the oldest element.
    Read all elements from the buffer and ensure they are in the correct order.


Started: Dec 09, 2023 @ 9:45am ET
Intervals: 1
Ended: Dec 09, 2023 @ 10:15am ET
"""


class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.head = 0 # read
        self.tail = 0 # write
        self.data = []

    def read(self, buffer, index=None):
        """Return the element at the head position.
        Move the head position forward (circularly).
        Handle cases where the buffer is empty."""
        if index is None:
            print(buffer.data)
        else:
            return buffer[index]

    def is_empty(buffer):
        pass

    def is_full(self, buffer, size):
        if len(buffer.data) == size:
            return True
        else:
            return False

    # TODO: what happens when tail > size?
    def write(self, buffer, value):
        """Add an element at the tail position.
        Move the tail position forward (circularly).
        If the buffer is full, either reject the new data or overwrite the oldest data (based on the mode set for the buffer)"""
        if self.is_full(buffer, buffer.size):
            raise Exception("Buffer is full.")
        else:
            buffer.data.insert(self.tail, value) 
            self.tail += 1


    # TODO: what happens when head > size?
    def overwrite(self, buffer, value):
       """If the buffer is full and a new element is written, overwrite the oldest element (at the head position)."""
       buffer.data[self.head] = value
       self.head += 1
       



if __name__ == '__main__':
    buffer = CircularBuffer(3)
    buffer.read(buffer)
    buffer.write(buffer, 10)
    buffer.read(buffer)
    buffer.write(buffer, 4)
    buffer.read(buffer)
    buffer.write(buffer, 7)
    buffer.read(buffer)
    
    #buffer should be full
    #buffer.write(buffer, 5)
    #buffer.read(buffer)
    
    #this should overwrite where HEAD is
    buffer.overwrite(buffer, 5)
    buffer.read(buffer)