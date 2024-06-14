__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Square Digits:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Started: June 14, 2024 @ 10:30am ET
Intervals: 1
Ended: June 14, 2024 @ 10:35am ET
"""
from sys import argv

def square_digits(number: int) -> int:
    squared_number = '' 

    for digit in str(number):
        squared_digit = int(digit)**2
        squared_number += str(squared_digit) 
    
    return squared_number

if __name__ == "__main__":
    number = int(argv[1])

    squared_number = square_digits(number)
    print(squared_number)
