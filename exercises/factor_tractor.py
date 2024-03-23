__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Factor Tractor:
Write a program to find all the prime factors of a given number. The program must return an array containing all the prime factors, sorted in ascending order. Remember that 1 is neither prime nor composite and should not be included in your output array.

Examples:
    primeFactorize(25) ➞ [5, 5]
    primeFactorize(19) ➞ [19]
    primeFactorize(77) ➞ [7, 11]

Started: Mar 23, 2024 @ 6:45am ET
Intervals: 1
Ended: March 23, 2024 @ 7:08am ET
"""
from sys import argv


def is_prime(n: int) -> bool:
    """ 
    Test if n a prime number

    Args: 
        n (int): the integer to test for primality
    
    Return:
        bool: True if n is a prime and False if n is not a prime
    """
    if n > 1:
        for i in range(2, (n // 2)):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def factorize(n: int) -> list:
    factors = []

    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
            i = i - 1
        i += 1      

    return factors

    # using sieve of Erastothenes
    """if n <= 2:
        return []
    sieve = [True]*(n + 1)

    for x in range(3, int(n**0.5) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2] + [i for i in range(3, n, 2) if sieve[i]]"""

if __name__ == "__main__":
    n = int(argv[1])
    
    factors = factorize(n)
    print(factors)