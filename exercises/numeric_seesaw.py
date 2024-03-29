__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Numeric Seesaw: 
A number is left-heavy if the digits on the left side are larger than the digits on the right. It is right-heavy if the digits on the right side are larger than the digits on the left. Else, it is balanced.

Create a function that takes in an integer and classifies it into one of the three mutually exclusive categories: left, right or balanced. For inputs with an odd number of integers, ignore the fulcrum (the middle number).

Examples:
    seesaw(3449) ➞ "right"
    // since 34 < 49

    seesaw(1143113) ➞ "left"
    // since 114 > 113 (3 is the fulcrum)

    seesaw(585585) ➞ "balanced"
    // since 585 == 585

Started: Mar 24, 2024 @ 5:50am ET
Intervals: 1
Ended: March 24, 2024 @ 6:01am ET
"""
from sys import argv

def seesaw(number: str) -> str:
    length = len(number)

    if length % 2 != 0:
        left = int(number[:length // 2])
        right = int(number[(length // 2) + 1:])
    else:
        left = int(number[:length // 2])
        right = int(number[length // 2:])

    if left > right:
        return "left"
    elif left < right:
        return "right"
    elif left == right:
        return "balanced"
    else:
        return "something went wrong"

if __name__ == "__main__":
    number = argv[1]

    result = seesaw(number)
    print(result)