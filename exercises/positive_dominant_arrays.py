__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
An array is positive dominant if it contains strictly more unique positive values than unique negative values. Write a function that returns true if an array is positive dominant.
Examples

isPositiveDominant([1, 1, 1, 1, -3, -4]) ➞ false
// There is only 1 unique positive value (1).
// There are 2 unique negative values (-3, -4).

isPositiveDominant([5, 99, 832, -3, -4]) ➞ true

isPositiveDominant([5, 0]) ➞ true

isPositiveDominant([0, -4, -1]) ➞ false

Start: 04:00am
End: 04:30am
Cycles: 1
"""
from sys import argv

def is_positive_dominant_int(array: list) -> bool:

    int_array = set([int(x) for x in array])
    positive_count = sum(1 for num in int_array if num > 0)
    negative_count = sum(1 for num in int_array if num < 0)

    if positive_count > negative_count:
        return True
    
    if positive_count < negative_count:
        return False

def is_positive_dominant_string(array: list) -> bool:

    unique_values = set(array)
    
    positive_count = sum(1 for value in unique_values if '-' not in value)
    negative_count = sum(1 for value in unique_values if '-' in value)

    if positive_count > negative_count:
        return True
    
    if positive_count < negative_count:
        return False

if __name__ == "__main__":
    string = argv[1]
    array = string.split(',')

    string_result = is_positive_dominant_string(array)
    int_result = is_positive_dominant_int(array)

    print(string_result)
    print(int_result)