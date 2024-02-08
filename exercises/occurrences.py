__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Occurrences:

Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five

Examples:
    Input:
    [19, 19, 15, 5, 3, 5, 5, 2] 19,19,15,5,3,5,5,2
    Output:
    True
    Input:
    [19, 15, 15, 5, 3, 3, 5, 2] 19,15,15,5,3,3,5,2
    Output:
    False
    Input:
    [19, 19, 5, 5, 5, 5, 5]
    Output:
    True

Started: Feb 08, 2024 @ 4:30am ET
Intervals: 1
Ended: Feb 08, 2024 @ 4:41am ET
"""
from sys import argv

def is_nineteen(numbers: list) -> bool:
    limit = 2

    if numbers.count('19') == limit:
        return True
    else:
        return False

def is_five(numbers: list) -> bool:
    limit = 3

    if numbers.count('5') == limit:
        return True
    else:
        return False

# TODO: is the more readable version more, less, or equally optimized as the return evaluation?
def find_occurrences(numbers: list) -> bool:
    if is_nineteen(numbers) and is_five(numbers):
        return True
    else:
        return False

"""
def find_occurrences(numbers: list) -> bool:
    return numbers.count('19') == 2 and numbers.count('5') == 3
"""


if __name__ == '__main__':
    numbers = argv[1].split(',')
    result = find_occurrences(numbers)

    print(result)