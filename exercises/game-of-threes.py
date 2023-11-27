#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Game of Threes: https://old.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/


The input is a single number: the number at which the game starts. Write a program that plays the Threes game, and outputs a valid sequence of steps you need to take to get to 1. Each step should be output as the number you start at, followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). The last line should simply be 1.

for 100:
    100 -1
    33 0
    11 1
    4 -1
    1

31337357

Started: Nov 27, 2023 @ 5:45am ET
Intervals: 1
Ended: Nov 27, 2023 @ 6:15am ET

"""

def is_divisible(n):
    if n % 3 == 0:
        return True
    else:
        return False

def test_divisibility(n):
    s = subtract(n)
    a = add(n)

    if is_divisible(s):
        print(n, "-1")
        return s
    elif is_divisible(a):
        print(n, "1")
        return a
    else:
        print("Could not add or substract")


def subtract(n):
    return n - 1

def add(n):
    return n + 1

def divide(n):
    return n // 3

# TODO: clean up printing 1 or -1 based on decision
if __name__ == '__main__':
    n = 31337357
    
    while n:
        divisible = is_divisible(n)
        #print(divisible)

        if n == 1:
            break

        if divisible == False:
            n = test_divisibility(n)
            #print(n, "1")
        else:
            n = divide(n)
            print(n, "0")
