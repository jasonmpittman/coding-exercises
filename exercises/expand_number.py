__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Expand Numbers:

Create a function that expands a number into a string as shown below:

25 ➞ "20 + 5"
70701 ➞ "70000 + 700 + 1"
685 ➞ "600 + 80 + 5"

    Examples

    expanded_form(70304) ➞ "70000 + 300 + 4"

    expanded_form(1037903) ➞ "1000000 + 30000 + 7000 + 900 + 3"

    expanded_form(802539) ➞ "800000 + 2000 + 500 + 30 + 9"

Started: Feb 09, 2025 @ 10:10am ET
Intervals: 1
Ended: Feb 09, 2025 @ 10:40am ET
"""
import sys

def expand_number(number):
    expanded_number = ''
    number_length = len(number)

    for i in range(number_length):
        if number[i] != '0':
            print(number[i] + '0'*(number_length - 1))
        
        number_length -= 1
    

if __name__ == "__main__":
    number = sys.argv[1]

    expand_number(number)
