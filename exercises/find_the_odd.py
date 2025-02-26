__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Find the odd:

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
    
    Examples

    [7] should return 7, because it occurs 1 time (which is odd).
    [0] should return 0, because it occurs 1 time (which is odd).
    [1,1,2] should return 2, because it occurs 1 time (which is odd).
    [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
    [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

Started: Feb 26th, 2025 @ 4:10pm ET (estimated)
Intervals: 1
Ended: Feb 26th, 2025 @ 4:19pm ET
"""

def find_the_odd(numbers: list) -> int:
    unique_numbers = set(numbers)
    odd_count = ''

    for unique_number in unique_numbers:
        if numbers.count(unique_number) % 2 != 0:
            odd_count = unique_number

    return odd_count

if __name__ == "__main__":
    numbers = [1,2,2,3,3,3,4,3,3,3,2,2,1]

    result = find_the_odd(numbers)

    if result != '':
        print(result)
    else:
        print("Something went wrong")