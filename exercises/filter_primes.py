__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Filter Primes:
Create a function that takes an array and returns a new array containing only prime numbers.

Examples

    filterPrimes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]

    filterPrimes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]

    filterPrimes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]

Started: Mar 12, 2024 @ 5:25pm ET
Intervals: 1
Ended: March 12, 2024 @ 5:55pm ET
"""
from sys import argv
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True


def filter_primes(numbers: list, mode=None) -> list:
    primeless = []

    if mode == None:
        # brute force method
        for number in numbers:
            if is_prime(number):
                primeless.append(number)
    
    return primeless



if __name__ == "__main__":
    numbers = list(map(int, argv[1].split(',')))

    print(filter_primes(numbers)) # 7,9,3,9,10,11,27 # 10007,1009,1007,27,147,77,1001,70 # 1009,10,10,10,3,33,9,4,1,61,63,69,1087,1091,1093,1097