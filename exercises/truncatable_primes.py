__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Truncatable Primes:
A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

    If the integer is only a left-truncatable prime, return "left".
    If the integer is only a right-truncatable prime, return "right".
    If the integer is both, return "both".
    Otherwise, return False.

Examples:
    truncatable(9137) ➞ "left"
    # Because 9137, 137, 37 and 7 are all prime.

    truncatable(5939) ➞ "right"
    # Because 5939, 593, 59 and 5 are all prime.

    truncatable(317) ➞ "both"
    # Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.


Started: Feb 17, 2024 @ 5:00am ET
Intervals: 1
Ended: Feb 17, 2024 @ 5:30am ET
"""
from sys import argv


if __name__ == "__main__":
    pass