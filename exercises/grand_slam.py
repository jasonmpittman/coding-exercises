__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Grand Sum: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Started: Feb 12, 2024 @ 4:05am ET
Intervals: 1
Ended: Feb 12, 2024 @ 4:19am ET
"""
import time

def sum_multiples_optimized(n: int) -> int:
    sum_of_multiples = sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)
    
    return sum_of_multiples

def get_multiples(n: int) -> list:
    multiples = []

    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    
    return multiples

def sum_multiples(multiples: list) -> int:
    total = 0

    for multiple in multiples:
        total += multiple
    
    return total

if __name__ == '__main__':
    n = 1000

    # unoptimized version
    start = time.time()
    multiples = get_multiples(n)
    total = sum_multiples(multiples)

    print(total)
    end = time.time()
    print("Execution time: ", (end-start) * 10**3)

    # optimized version
    start = time.time()
    total = sum_multiples_optimized(n)
    print(total)
    end = time.time()
    print("Execution time: ", (end-start) * 10**3)
