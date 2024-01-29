__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Persistence:
The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.

The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.

Create two functions that take an integer as an argument and:

    Return its additive persistence.
    Return its multiplicative persistence.

Started: Jan 29, 2024 @ 5:05am ET
Intervals: 1
Ended: Jan 29, 2024 @ 5:35am ET
"""
from sys import argv

def get_numbers(n: str) -> list:
    numbers = []
    for c in n:
        numbers.append(int(c))
    
    return numbers

# TODO: need loop to continue additive logic
def compute_additive_persistance(n: str) -> int:
    additive_persistence = 0
    counter = 0
    numbers = get_numbers(n)
    

    additive_persistence = sum(numbers)
    counter += 1


    return counter

def compute_multiplicative_persistence(n: str) -> int:
    multiplicative_persistence = 0
    numbers = get_numbers(n)

    print(numbers)

    return multiplicative_persistence

if __name__ == '__main__':
    n = argv[1]

    print(compute_additive_persistance(n))
    #compute_multiplicative_persistence(n)
