__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Frequency Sort: 
Create a function that takes an array of integers arr and sort the elements of the array by decreasing frequency of the elements. If two elements have the same frequency, sort them by increasing value.

Examples:
    sortFreq([2, 3, 5, 3, 7, 9, 5, 3, 7]) ➞ [3, 3, 3, 5, 5, 7, 7, 2, 9]
    sortFreq([1, 2, 3, 0, 5, 0, 1, 6, 8, 8, 6, 9, 1]) ➞ [1, 1, 1, 0, 0, 6, 6, 8, 8, 2, 3, 5, 9]
    sortFreq([4, 4, 2, 5, 1, 1, 3, 3, 2, 8]) ➞ [1, 1, 2, 2, 3, 3, 4, 4, 5, 8]

Started: Feb 06, 2024 @ 6:30am ET
Intervals: 1
Ended: Feb 06, 2024 @ 7:00am ET
"""
from sys import argv
import operator

#TODO: output is a tuple of k,v but is technically correct
def sort_by_frequency(numbers: list) -> list:
    frequency_of_numbers = {}
    sorted_numbers = []

    for number in numbers:
        if number not in frequency_of_numbers.keys():
            frequency_of_numbers[number] = numbers.count(number)

    sorted_numbers = sorted(frequency_of_numbers.items(), key=operator.itemgetter(1), reverse=True)


    print(frequency_of_numbers)
    print(sorted_numbers)

if __name__ == '__main__':
    # 2,3,5,3,7,9,5,3,7
    numbers = argv[1].split(',')
    sort_by_frequency(numbers)