__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Billboard:
A billboard is an m * n array, where each array element consists of either one letter or a blank space. You are given a phrase and the billboard dimensions. Create a function that determines whether you can place the complete phrase on the billboard.

There are two rules:

    If there is a space between two words:
        If they are on the same row, you must put a space.
        If they are two different rows, the space is optional.
    You can only put COMPLETE words on a row.

Started: April 03, 2024 @ 5:05am ET
Intervals: 1
Ended: April 03, 2024 @ 5:28am ET
"""
from sys import argv


def check_billboard(string: str, rows: int, columns: int) -> bool:
    string_size = len(string)

    # Check if the entire string can fit on a single row
    if rows == 1 and string_size <= columns:
        return True

    # Check if the string can fit on multiple rows
    if ' ' in string and rows >= 2:
        strings = string.split(' ')
        if len(strings[0]) <= columns and len(strings[1]) <= columns:
            return True

    return False

if __name__ == "__main__":
    string = argv[1]
    rows = int(argv[2])
    columns = int(argv[3])

    is_fit = check_billboard(string, rows, columns)
    print(is_fit)