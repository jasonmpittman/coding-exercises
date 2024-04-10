__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Narcissistic Number:
A Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example, take 153 (3 digits), which is narcisstic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
    1652 (4 digits), is non-narcisstic:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
 
Create a function that returns true or false depending upon whether the given number n is a Narcissistic number or not.

Started: April 10, 2024 @ 7:25am ET
Intervals: 1
Ended: April 10, 2024 @ 7:36am ET
"""
from sys import argv

def is_narcissistic_opt(number: str) -> bool:
    """An optimized version of the function"""
    length = len(number)

    narcissistic_sum = sum(int(digit) ** length for digit in number)
    return narcissistic_sum == int(number)

def is_narcissistic(number: str) -> bool:
    """A standard logic implementation"""
    length = len(number)
    result = 0

    for n in number:
        result = result + int(n)**length

    if result == int(number):
        return True
    else:
        return False

if __name__ == "__main__":
    number = argv[1]

    print(is_narcissistic(number))
    print(is_narcissistic_opt(number))