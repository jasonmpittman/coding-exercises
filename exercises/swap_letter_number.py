__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Swap Letter with Numbers:
given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
    
    Example

    Input = "The sunset sets at twelve o' clock."
    Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


Started: Mar 2nd, 2025 @ 3:25am ET (estimated)
Intervals: 1
Ended: Mar 2nd, 2025 @ 3:39am ET
"""

def convert_string_to_number(input: str) -> str:
    string = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(string)
    converted_string = ''

    for i in input.lower():
        if i in alphabet:
            value = alphabet.index(i)
            converted_string += ' ' + str(value + 1)
    
    print(converted_string)


if __name__ == "__main__":
    input = "The sunset sets at twelve o' clock."
    convert_string_to_number(input)