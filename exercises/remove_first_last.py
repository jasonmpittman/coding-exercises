
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
write a function that removes the first and last characters of a string. You're given one parameter, the original string.

Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.
Examples

'eloquent' --> 'loquen'
'country'  --> 'ountr' 
'person'   --> 'erso'
'ab'       --> '' (empty string)
'xyz'      --> 'y'

Start: 10:25pm
End: 10:29pm
Cycles: 1
"""
from sys import argv


def remove_first_and_last(string: str) -> str:
    """ remove the first and last characters from a string """

    if len(string) >= 2:
        return string[1:len(string) - 1:]
    else:
        return None

if __name__ == "__main__":
    string = argv[1]

    result = remove_first_and_last(string)
    print(result)


