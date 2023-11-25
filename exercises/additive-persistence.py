#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Additive Persistence: https://old.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

calculate the additive persistence of a number, defined as how many loops you have to do summing its digits until you get a single digit number. Take an integer N:

    Add its digits
    Repeat until the result has 1 digit

The total number of iterations is the additive persistence of N. 

13 -> 1
1234 -> 2
9876 -> 2
199 -> 3

Started: Nov 25, 2023 @ 1:35pm ET
Intervals: 1
Ended: Nov 25, 2023 @ 2:05pm ET

"""

def get_number():
    number = int(input('Enter a number: '))

    return number

def add_digits(number):
    total = 0

    while number:
        total += number % 10
        number //= 10
    
    return total

def add_persistence(number):
    additions = 1

    while number > 9:
        number = add_digits(number)
        additions += 1
    
    return additions

if __name__ == '__main__':
    number = get_number()
    print(number)
    
    total = add_digits(number)
    print(total)
    
    additions = add_persistence(total)
    print(additions)
