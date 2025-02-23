__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Multiples of 3 or 5:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Part One: develop rule generator
Started: Feb 24th, 2025 @ 07:05am ET
Intervals: 1
Ended: Feb 24th, 2025 @ 7:35am ET
"""
import sys

def get_multiples(n: int) -> list:
    multiples = [n for n in range(1, n) if n % 3 == 0 or n % 5 == 0]
    
    return multiples

def get_sum(multiples: list) -> int:
    s = 0
    
    for m in multiples:
        s = s + m
    
    print(s)

if __name__ == "__main__":
    n = int(sys.argv[1])

    if n < 0:
        print(0)
    else:
        multiples = get_multiples(n)
        get_sum(multiples)