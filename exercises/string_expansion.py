__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" String Expansion:
Given a string that includes alphanumeric characters ("3a4B2d") return the expansion of that string: The numeric values represent the occurrence of each letter preceding that numeric value. There should be no numeric characters in the final string.

Examples:
    "3D2a5d2f"  -->  "DDDaadddddff"    # basic example: 3 * "D" + 2 * "a" + 5 * "d" + 2 * "f"
    "3abc"      -->  "aaabbbccc"       # not "aaabc", nor "abcabcabc"; 3 * "a" + 3 * "b" + 3 * "c"
    "3d332f2a"  -->  "dddffaa"         # multiple consecutive digits: 3 * "d" + 2 * "f" + 2 * "a"
    "abcde"     -->  "abcde"           # no digits
    "1111"      -->  ""                # no characters to repeat
    ""          -->  ""                # empty string

Started: May 28, 2024 @ 7:40am ET
Intervals: 1
Ended: May 28, 2024 @ 7:45am ET
"""
from sys import argv

def expand_string(string: str) -> str:
    expanded_string = ''
    numerals = [str(x) for x in range(1,10)]

    #for character in string:
    for i in range(len(string)):
        if string[i] in numerals and string[i + 1] not in numerals:
            expanded_string += int(string[i]) * string[i + 1]
        elif string[i] not in numerals:
            expanded_string += string[i] 

    return expanded_string


if __name__ == "__main__":
    string = argv[1]

    expanded_string = expand_string(string)
    print(expanded_string)