__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
You are given two characters (s, r), and a string (a) terminated with \0.

Replace all occurrences of s in a by r.

Example:
    Example: replaceAll [1,2,2] 1 2 -> in list [1,2,2] we replace 1 with 2 to get new list [2,2,2]

Start: 5:55pm
End: 06:00pm
Cycles: 1
"""
from sys import argv

def replace_all(string: str, s: str, r: str) -> str:
    new_string = ''

    for char in string:
        if char == s:
            new_string += r
        else:
            new_string += char

    return new_string


if __name__ == "__main__":
    string = argv[1]
    s = argv[2]
    r = argv[3]

    result = replace_all(string, s, r)
    print(result)
