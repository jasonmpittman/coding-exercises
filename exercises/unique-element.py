#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Unique Element:

Write a function that finds the element that appears exactly once in an array where every other element appears exactly twice. The array will contain integers, and you can assume that there is always exactly one element that appears only once.

    findUniqueElement([4, 3, 2, 4, 3]) should return 2.
    findUniqueElement([7, 3, 5, 5, 4, 3, 4]) should return 7.

    43243
    7355434
    
Started: Dec 08, 2023 @ 5:10am ET
Intervals: 1
Ended: Dec 08, 2023 @ 5:40am ET
"""

from sys import argv

def find_unqiue_element(array: int) -> int:
    """
    1. Initialize Result: Start with a variable, say result, initialized to 0.
    2. Iterate and XOR: Iterate through each element in the array. Perform a XOR operation between the result and the current element. Update result with this new value.
        a. Operation: result = result ^ currentElement
    3. Final Result: After completing the iteration, result will hold the value of the unique element. This happens because all elements that appear twice will cancel themselves out (due to the self-inverting property), leaving only the unique element.
    """
    result = 0
    current = 0
    
    for i in map(int, array):
        current = i
        result = result ^ current

    
    return result


if __name__ == '__main__':
    array = list(argv[1])
    result = find_unqiue_element(array)

    print(result)