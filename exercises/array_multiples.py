__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Array Multiples:
Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length.

Examples:
    ArrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]
    ArrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    ArrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

Started: Jan 05, 2024 @ 3:35am ET
Intervals: 1
Ended: Jan 05, 2024 @ 3:40am ET
"""

from sys import argv

def calculate_multiple(n: int, i: int) -> int:
    return n * i

def build_array_of_multiples(num: int, length: int) -> list:
    array_of_multiples = []
    i = 1

    for _ in range(length):
        multiple = calculate_multiple(num, i)
        array_of_multiples.append(multiple)
        i += 1

    return array_of_multiples

if __name__ == '__main__':
    num, length = argv[1].split(',')
    
    print(build_array_of_multiples(int(num), int(length)))