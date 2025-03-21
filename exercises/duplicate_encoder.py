__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Duplicate Encoder:
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 


Started: Mar 7th, 2025 @ 6:25am ET (estimated)
Intervals: 1
Ended: Mar 7th, 2025 @ 6:28am ET
"""
import sys

def encode_duplicates(string: str) -> str:
    encoded_string = ''

    for char in string:
        if string.count(char) >= 2:
            encoded_string += ')'
        else:
            encoded_string += '('

    return encoded_string


if __name__ == "__main__":
    string = sys.argv[1]

    encoded_string = encode_duplicates(string)
    print(encoded_string)