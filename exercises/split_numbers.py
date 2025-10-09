__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that takes a number num and returns each place value in the number.

Examples
    num_split(39) ➞ [30, 9]
    num_split(-434) ➞ [-400, -30, -4]
    num_split(100) ➞ [100, 0, 0]

Start: 04:40am
End: 04:58:am
Cycles: 1
"""
from sys import argv

def num_split(num: str) -> list:
    numbers = []
    l = len(num) - 1

    for i in range(len(num)):
        numbers.append(num[i] + ('0' * l))
        l -= 1

    return numbers

if __name__ == "__main__":
    num = argv[1]

    numbers = num_split(num)
    print(numbers)