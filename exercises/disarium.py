__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Disarium:
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples:
    is_disarium(75) ➞ False
    # 7^1 + 5^2 = 7 + 25 = 32
    is_disarium(135) ➞ True
    # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

    is_disarium(544) ➞ False
    is_disarium(518) ➞ True
    is_disarium(466) ➞ False
    is_disarium(8) ➞ True

Started: Jan 04, 2024 @ 6:00am ET
Intervals: 1
Ended: Jan 04, 2024 @ 6:07am ET
"""
from sys import argv

def convert_to_numbers(n: str) -> list:
    numbers = []

    for number in n:
        numbers.append(int(number))
    
    return numbers

def is_disarium(n):
    total = 0
    e = 1
    numbers = convert_to_numbers(n)

    for number in numbers:
        total += number ** e
        e += 1

    if total == int(n):
        return True
    else:
        return False
    

if __name__ == '__main__':
    n = argv[1]

    print(is_disarium(n))