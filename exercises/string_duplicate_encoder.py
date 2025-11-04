__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
    "din"      =>  "((("
    "recede"   =>  "()()()"
    "Success"  =>  ")())())"
    "(( @"     =>  "))((" 

Start: 4:40am
End: 04:45am
Cycles: 1
"""
from sys import argv

def get_letter_count(string: str, letter: str) -> int:
    return string.count(letter) 

def encode(string: str) -> str:
    encoded_string = ''

    for letter in string:
        if get_letter_count(string, letter) > 1:
            encoded_string += ')'
        else:
            encoded_string += '('

    return encoded_string

if __name__ == "__main__":
    plain_string = argv[1]

    result = encode(plain_string.lower())
    print(result)


