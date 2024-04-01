__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Bit Masking:
Bit masking is a technique used to "hide" certain parts of a number. It's great to use if you want to convey lots of information in a single integer. It takes a number n, converts it to its binary form, and then returns the digit at the index b of that binary number. Note that digit 0 is really the last digit since the least significant (smallest) digit is last. Your job is to create a function bit_mask that takes two arguments - the first being n and the second b - and returns the "masked" form of n.
Examples

bit_mask(37, 2) -> 1
# Binary representation is this:
# 0b100101
#      ^
# We return index 2 from the right, which is 1

bit_mask(56, 1) -> 0
# 0b111000
#        ^

bit_mask(327, 6) -> 1
# 0b101000111
#     ^

Started: April 01, 2024 @ 7:05am ET
Intervals: 1
Ended: April 01, 2024 @ 7:35am ET
"""
from sys import argv



if __name__ == "__main__":
    integer = int(argv[1])
    mask = int(argv[2])

    # neat trick to get a binary string
    b = "{0:b}".format(integer)
    
    # little hack to get index from right
    index = (len(b) - mask) - 1
    
    print(b[index])