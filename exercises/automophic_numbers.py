__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Automorphic Numbers:
Create a function that takes a number and returns true if the number is automorphic, false if it isn't.

A number nis automorphic if n^2ends in n

Example:
    isAutomorphic(5) ➞ true
    isAutomorphic(8) ➞ false
    isAutomorphic(76) ➞ true

Started: Jan 02, 2024 @ 5:45am ET
Intervals: 1
Ended: Jan 02, 2024 @ 6:15am ET
"""
from sys import argv

# this feels rather hacked with all the type casting?
def is_automorphic(n: int) -> bool:
    square = n**2
    square_string = str(square)
    size = len(str(n)) * -1

    print(square_string[size:])

    if size == -1:
        if str(square_string[-1]) == str(n):
            print(square_string, square_string[-1])
            return True
        else:
            print(square_string, square_string[-1])
            return False
    else:
        if str(square_string[size:]) == str(n):
            print(square_string, square_string[size:])
            return True
        else:
            print(square_string, square_string[size:])
            return False


if __name__ == '__main__':
    n = int(argv[1])
    
    print(is_automorphic(n))