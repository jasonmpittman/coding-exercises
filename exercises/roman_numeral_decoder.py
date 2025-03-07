__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Roman Number Decoder:
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
    Example:

    "MM"      -> 2000
    "MDCLXVI" -> 1666
    "M"       -> 1000
    "CD"      ->  400
    "XC"      ->   90
    "XL"      ->   40
    "I"       ->    1

Started: Mar 8th, 2025 @ 8:52am ET (estimated)
Intervals: 1
Ended: Mar 8th, 2025 @ 9:03am ET
"""
import sys

def convert_roman_to_integer(numberals):
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for r in reversed(numberals):  # Iterate through the string in reverse order
        value = roman_numbers[r]
        if value < prev_value:
            # If the current value is less than the previous value, subtract it
            total -= value
        else:
            # Otherwise, add it to the total
            total += value
            prev_value = value

    return total

if __name__ == "__main__":
    numerals = sys.argv[1]

    decoded_value = convert_roman_to_integer(numerals)
    print(decoded_value)