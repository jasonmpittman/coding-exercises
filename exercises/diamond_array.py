__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that returns an array that expands by 1 from 1 to the value of the input, and then reduces back to 1. Items in the arrays will be the same as the length of the arrays.

Examples
    diamondArrays(1) ➞ [[1]]
    diamondArrays(2) ➞ [[1], [2, 2], [1]]
    diamondArrays(5) ➞ [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3], [2, 2], [1]]

Start: 8:45am
End: am
Cycles: 1
"""
import sys

def build_input_list(input: str) -> list:
    i = 1
    input_list = []

    while i <= int(input):
        input_list.append(i)
        i += 1

    return input_list

def create_diamond_array(input: str) -> list:
    array_count = input
    outer_array = []
    input_list = build_input_list(input)


if __name__ == "__main__":
    input = sys.argv[1]
    create_diamond_array(input)