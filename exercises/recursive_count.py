__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that recursively counts the integer's number of digits.

Examples
    count(318) ➞ 3
    count(-92563) ➞ 5
    count(4666) ➞ 4
    count(-314890) ➞ 6
    count(654321) ➞ 6
    count(638476) ➞ 6

Start: 5:40am
End: 5:46:am
Cycles: 1
"""

from sys import argv

def count_digits(digits: list) -> int:
    if not digits:
        return 0
    else:
        return 1 + count_digits(digits[1:])    


if __name__ == "__main__":
    number = list(argv[1])

    result = count_digits(number)
    print(result)


