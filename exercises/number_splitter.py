__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.

Examples
    number_split(4) ➞ [2, 2]
    number_split(10) ➞ [5, 5]
    number_split(11) ➞ [5, 6]
    number_split(-9) ➞ [-5, -4]

Start: 04:45am
End: 04:54:am
Cycles: 1
"""
from sys import argv

def split_number(number: int) -> list:
    if number % 2 == 0:
        number_parts = [int(number / 2), int(number / 2)]
    elif number > 0:
        number_parts = [int(number / 2), int(number /2) + 1]
    elif number < 0:
        number_parts = [int(number / 2) + -1, int(number /2)]

    return number_parts

if __name__ == "__main__":
    number = int(argv[1])

    result = split_number(number)
    print(result)