__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Digit by Digit Number:
Implement a class that allows chaining methods zero, one, two, three, four, five, six, seven, eight, nine to construct numbers in a similar manner.

Note: your class should also support a method which converts its instances into integers (provided in the initial solution).

Example:
    731 you could write fancy Num.seven.three.one!

Started: Mar 1st, 2025 @ 7:15am ET (estimated)
Intervals: 1
Ended: Mar 1st, 2025 @ 7:34am ET
"""
import sys

word_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    }

number_map = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}


def convert_int_to_words(number: str) -> str:
    converted_number = 'Num'

    for n in number:
        converted_number = converted_number + '.' + number_map[int(n)]

    print(converted_number)

if __name__ == "__main__":
    number = sys.argv[1]
    convert_int_to_words(number)