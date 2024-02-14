__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Odds and Evens:

Write a function that takes a list of numbers and returns a list with two elements:

    The first element should be the sum of all even numbers in the list.
    The second element should be the sum of all odd numbers in the list.

Examples:
    sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
    # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

    sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

    sum_odd_and_even([0, 0]) ➞ [0, 0])

Started: Feb 14, 2024 @ 4:55am ET
Intervals: 1
Ended: Feb 14, 2024 @ 5:25am ET
"""
from sys import argv

def sum_odds_and_evens(numbers: list) -> list:
    odds = []
    evens = []

    for number in numbers:
        if int(number) % 2 == 0:
            evens.append(int(number))
        else: 
            odds.append(int(number))
    
    return [sum(evens), sum(odds)]

if __name__ == '__main__':
    numbers = argv[1].split(',') # 1,2,3,4,5,6

    sums = sum_odds_and_evens(numbers)
    print(sums)