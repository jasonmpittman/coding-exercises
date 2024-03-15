__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Alternating Binary:
Write a function that returns true if the binary string can be rearranged to form a string of alternating 0s and 1s.

Examples

    canAlternate("0001111") ➞ true
    // Can make: "1010101"
    canAlternate("01001") ➞ true
    // Can make: "01010"
    canAlternate("010001") ➞ false
    canAlternate("1111") ➞ false

Started: Mar 15, 2024 @ 5:15am ET
Intervals: 1
Ended: March 15, 2024 @ 5:25am ET
"""
from sys import argv
import re

def is_even(count: int) -> bool:
    return True if count % 2 == 0 else False

def can_alternate(string: str) -> bool:
    
    # obvious false conditions
    if "0" not in string or "1" not in string:
        return False

    zeroes = string.count("0")
    ones = string.count("1")

    # alternating binary is only true when either 0 or 1 is even but the other is not even
    if (is_even(zeroes) or is_even(ones)) and (not is_even(zeroes) or not is_even(ones)):
        return True
    else:
        return False


if __name__ == "__main__":
    string = argv[1]
    result = can_alternate(string)

    print(result)