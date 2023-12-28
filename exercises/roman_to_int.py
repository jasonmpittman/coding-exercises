__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Roman to Integer:
Write a Python function that converts a Roman numeral to an integer. Roman numerals are represented by combinations of letters from the Latin alphabet (I, V, X, L, C, D, M) which represent values 1, 5, 10, 50, 100, 500, and 1000, respectively.

Given a string representing a Roman numeral, convert it to an integer. The Roman numeral is guaranteed to be within the range from 1 to 3999 (I to MMMCMXCIX).

Example:

    Input: "IX"
    Output: 9
    Explanation: IX is a Roman numeral for 9.

Tests:
    III (3)
    LVIII (58)
    MCMXCIV (1994)

Started: Dec 28, 2023 @ 6:45am ET
Intervals: 1
Ended: Dec 28, 2023 @ 7:15am ET
"""
from sys import argv

def convert_roman_to_integer(roman):
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

    for r in reversed(roman):  # Iterate through the string in reverse order
        value = roman_numbers[r]
        if value < prev_value:
            # If the current value is less than the previous value, subtract it
            total -= value
        else:
            # Otherwise, add it to the total
            total += value
            prev_value = value

    return total

if __name__ == '__main__':
    roman = argv[1]
    
    print(convert_roman_to_integer(roman))