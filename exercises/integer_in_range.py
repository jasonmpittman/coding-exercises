__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Integer in Range:
Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.

Examples:
    intWithinBounds(3, 1, 9) ➞ true
    intWithinBounds(6, 1, 6) ➞ false
    intWithinBounds(4.5, 3, 8) ➞ false

Started: Mar 10, 2024 @ 6:50pm ET
Intervals: 1
Ended: March 10, 2024 @ 7:00pm ET
"""
from sys import argv


def is_within_bounds(n: int, lower: int, upper: int) -> bool:

    if n >= lower and n < upper:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        n = int(argv[1])
        lower = int(argv[2])
        upper = int(argv[3])

        result = is_within_bounds(n, lower, upper)
        print(result)
    
    except ValueError:
        print(False)

