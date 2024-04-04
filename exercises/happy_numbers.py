__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Happy Numbers:
A 1 is unhappy if the digit to its left and the digit to its right are both 0s. A 0 is unhappy if the digit to its left and the digit to its right are both 1s. If a number has only one neighbor, it is unhappy if its only neighbor is different. Otherwise, a number is happy.

Write a function that takes in an array of 0s and 1s and outputs the portion of numbers which are happy. The total portion of numbers which are happy can be represented as: portion of happy numbers = (happy 0s + happy 1s) / total numbers

Examples:
    portionHappy([0, 1, 0, 1, 0]) ➞ 0
    portionHappy([0, 1, 1, 0]) ➞ 0.5
    portionHappy([0, 0, 0, 1, 1]) ➞ 1
    portionHappy([1, 0, 0, 1, 1]) ➞ 0.8

Started: April 04, 2024 @ 5:15am ET
Intervals: 1
Ended: April 04, 2024 @ 5:45am ET
"""
from sys import argv

def is_happy(index, array):
    #check first element in array
    if index == 0:
        if array[index] == '0' and array[index + 1] == '1':
            return False 
        elif array[index] == '1' and array[index + 1] == '0':
            return False
        else:
            return True
    
    #check last element in array
    if index == len(array) - 1:
        if array[index] == '0' and array[index - 1] == '1':
            return False
        elif array[index] == '1' and array[index - 1] == '0':
            return False
        else:
            return True

    #check middle elements in array
    if index in range(1, len(array) - 1):
        if array[index] == '0' and array[index - 1] == '1' and array[index + 1] == '1':
            return False
        elif array[index] == '1' and array[index - 1] == '0' and array[index + 1] == '0':
            return False
        else:
            return True

def calculate_portion(zeroes: int, ones: int, total: int) -> int:
    return (zeroes + ones) / total


if __name__ == "__main__":
    array = argv[1].split(',') # 0,1,0,1,0  0,0,0,1,1   1,0,0,1,1

    size = len(array)
    zeroes = 0
    ones = 0

    for i in range(0, size - 1):
        result = is_happy(i, array)

        if array[i] == '0' and result == True:
            zeroes += 1
        elif array[i] == '1' and result == True:
            ones += 1

    portion = calculate_portion(zeroes, ones, size)
    print(portion)