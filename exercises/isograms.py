__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Isograms: 
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

    Example: (Input --> Output)

    "Dermatoglyphics" --> true
    "aba" --> false
    "moOse" --> false (ignore letter case)

Started: Mar 3rd, 2025 @ 7:40am ET (estimated)
Intervals: 1
Ended: Mar 3rd, 2025 @ 7:55am ET
"""
import sys

def is_isogram(string: str) -> bool:

    for letter in string:
        if string.count(letter) > 1:
            return False

    return True


if __name__ == "__main__":
    string = sys.argv[1].lower()
    result = is_isogram(string)

    print(result)