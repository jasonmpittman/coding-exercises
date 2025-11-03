__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Given a string of length >= 2, repeat every character between the first and last character twice.

Examples
    blur('af') -> 'af'
    blur('asf') -> 'assf'
    blur('asdf') -> 'assddf'
    blur('fieowg') -> 'fiieeoowwg'

Start: 8:30am
End: 08:37am
Cycles: 1
"""
from sys import argv

def get_middle(string: str) -> str:
    return string[1:len(string) - 1]

def blur(string: str) -> str:
    blurred_string = ''
    

    if len(string) > 2:
        blurred_string += string[0]
        middle_substring = get_middle(string)
        
        for char in middle_substring:
            blurred_string += char * 2
        
        blurred_string += string[len(string) - 1]
    else:
        return string

    return blurred_string


if __name__ == "__main__":
    string = argv[1]

    result = blur(string)
    print(result)

