__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Prime Search:

Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".

Examples:
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

is_prime(primes, 3) ➞ "yes"
is_prime(primes, 4) ➞ "no"
is_prime(primes, 67) ➞ "yes"
is_prime(primes, 36) ➞ "no"

Started: Jan 11, 2024 @ 6:15am ET
Intervals: 1
Ended: Jan 11, 2024 @ 6:40am ET
"""
from sys import argv

def is_prime(primes: list, n: int) -> str:
    """ Implements a binary search algorithm """
    first_index = 0
    middle_index = len(primes) // 2
    last_index = len(primes) - 1

    while 1 <= len(primes) - 1:

        if n == primes[middle_index]:
            return "yes"

        if n > primes[middle_index]:
            primes = primes[middle_index:last_index + 1]
            middle_index = len(primes) // 2
        
        if n < primes[middle_index]:
            primes = primes[first_index:middle_index]
            middle_index = len(primes) // 2
        
        print(primes)

    return "no"


if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    n = int(argv[1])

    print(is_prime(primes, n))

