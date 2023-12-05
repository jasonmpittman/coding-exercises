#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Fibonacci-ish: https://old.reddit.com/r/dailyprogrammer/comments/3opin7/20151014_challenge_236_intermediate_fibonacciish/

The Fibonacci Sequence is a famous integer series in the field of mathematics. The sequence is recursively defined for n > 1 by the formula f(n) = f(n-1) + f(n-2). In plain english, each term in the sequence is found by adding the previous two terms together. Given the starting values of f(0) = 0 and f(1) = 1 the first ten terms of the sequence are:

    0 1 1 2 3 5 8 13 21 34

We will notice however that some numbers are left out of the sequence and don't get any of the fame, 9 is an example. However, if we were to start the sequence with a different value for f(1) we will generate a new sequence of numbers. Here is the series for f(1) = 3:

    0 3 3 6 9 15 24 39 102 165

We now have a sequence that contains the number 9. What joy!

Today you will write a program that will find the lowest positive integer for f(1) that will generate a Fibonacci-ish sequence containing the desired integer (let's call it x).

Your input will be a single positive integer x.

Sample Input 1: 21

Sample Input 2: 84 

The sequence of integers generated using the recursion relation starting from 0 and ending at the desired integer x with the lowest value of f(1).

Sample Output 1: 0 1 1 2 3 5 8 13 21

Sample Output 2: 0 4 4 8 12 20 32 52 84

    Challenge Input:
    Input 1: 0
    Input 2: 578
    Input 3: 123456789

Started: Dec 05, 2023 @ 4:15am ET
Intervals: 1
Ended: Dec 05, 2023 @ 4:45am ET 
"""

from sys import argv
 
def generate_sequence(start, end):
    sequence = [0, start]

    while sequence[-1] < end: # as long as the last element is less than n
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence
    
# TODO: finish find feature
def find_sequence(n):
    start = 1
    if n == 0:
        print("0")
        return
    else:
        # do while to find lowest starting number containing n as last element
        sequence = generate_sequence(start, n)
        print(sequence)



if __name__ == '__main__':
    n = int(argv[1])
    find_sequence(n) # this prints a correct sequence