__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Bit Counting:

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


Started: Feb 27th, 2025 @ 05:30am ET
Intervals: 1
Ended: Feb 27th, 2025 @ 5:38am ET
"""
import sys

def count_bits(bits: str) -> int:
    return bits.count('1')

def convert_to_bits(number: int) -> str:
    return format(number, '08b')

if __name__ == "__main__":
    number = int(sys.argv[1])
    bits = convert_to_bits(number)
    count = count_bits(bits)

    print(count)