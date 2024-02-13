__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Prime Factors:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Started: Feb 13, 2024 @ 5:30am ET
Intervals: 1
Ended: Feb 13, 2024 @ 5:52am ET
"""
from sys import argv


def find_largest_prime(n: int) -> int:
    """Implements a naive division approach"""
    divisor = 2
    while divisor < n:
        if n % divisor == 0 and n / divisor > 1:
            n = n / divisor
            divisor = 2
        else:
            divisor += 1
        
    return int(n)



if __name__ == '__main__':
    n = int(argv[1])

    largest_prime = find_largest_prime(n)
    print(largest_prime)


