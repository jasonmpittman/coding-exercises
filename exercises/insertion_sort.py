__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Insertion Sort:

Given an integer array, in-place sort it without using any inbuilt functions.

Input : [6, 3, 4, 8, 2, 9]
Output: [2, 3, 4, 6, 8, 9]

Input : [9, -3, 5, -2, -8, -6]
Output: [-8, -6, -3, -2, 5, 9]


Started: Mar 05, 2024 @ 3:50am ET
Intervals: 1
Ended: Marc 05, 2024 @ 4:05am ET
"""
from sys import argv


def sort_by_insertion(array: list) -> list:
    length = len(array)

    if length == 0 or length == 1:
        return array

    for i in range(1, length):
        current_element = array[i]
        selected_element_index = i - 1
        print("Current element is {} and selected index is {}".format(current_element, selected_element_index))

        while selected_element_index >= 0 and current_element < array[selected_element_index]:
            array[selected_element_index + 1] = array[selected_element_index]
            selected_element_index -= 1
        
        array[selected_element_index + 1] = current_element

    return array
        


if __name__ == "__main__": # 6,3,4,8,2,9 # 9,-3,5,-2,-8,-6
    array = list(map(int, argv[1].split(',')))
    
    sorted_array = sort_by_insertion(array)
    print(sorted_array)
