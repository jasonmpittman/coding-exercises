#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Letter Value Sum: https://old.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.

Started: Nov 24, 2023 @ 4:45pm ET
Intervals: 1
Ended: Nov 24, 2023 @ 4:45pm ET

"""

from sys import argv

def get_letter_value(l):
    return ord(l) - 96

if __name__ == "__main__":
    word = argv[1]
    sum = 0

    for l in word:
        sum += get_letter_value(l)
    
    print(sum)
