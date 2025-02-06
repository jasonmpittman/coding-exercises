__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Radix Sort:

Python has a beautiful built-in function sorted that sorts an iterable, usually an array of numbers, sorting them in ascending order, but using key= you can sort the iterable in different ways.

Create a function that takes an array of integers as an argument and returns the same array in ascending order. Using sorted() would be easy, but for this challenge YOU have to sort the array creating your own algorithm.

    Examples

    sort_array([2, -5, 1, 4, 7, 8]) ➞ [-5, 1, 2, 4, 7, 8]

    sort_array([23, 15, 34, 17, -28]) ➞ [-28, 15, 17, 23, 34]

    sort_array([38, 57, 45, 18, 47, 39]) ➞ [18, 38, 39, 45, 47, 57]

Started: Feb 07, 2025 @ 4:40am ET
Intervals: 1
Ended: Feb 07, 2025 @ 5:00am ET
"""

from os import wait

# TODO: list index out of range line 51
def sort_by_msd(array):
    max_value = max(array)
    array_length = max_value + 1
    
    # generate number of needed buckets
    buckets = [0] * array_length 

    # same for end state sorted array
    sorted_array = [0] * len(array) 


    # frequency count 
    for a in array:
        buckets[a] += 1        

    for i in range(1, array_length):
        buckets[i] += buckets[i - 1]

    i = array_length - 1
    while i >= 0:
        current_a = array[i]
        buckets[current_a] -= 1
        position = buckets[i]
        sorted_array = current_a
        i -= 1

    return sorted_array

if __name__ == "__main__":
    #array = [38, 57, 45, 18, 47, 39]
    array = [2,2,0,6,1,9,9,7]

    sorted_array = sort_by_msd(array)
    print(sorted_array)
