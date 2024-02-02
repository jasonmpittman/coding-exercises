__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Legendre's Formula: https://edabit.com/challenge/2mtNE8cRcctgBCPZw

Legendre's formula finds the exponent of the largest power of some prime p that divides (is a factor of) the factorial of some number n.

Stated differently, given an integer n and a prime number p, find the largest x such that p^x (p raised to power x) divides n! (factorial) 

Examples:
    legendre(5, 100) ➞ 24
    legendre(2, 128) ➞ 127
    legendre(3, 50) ➞ 22


Started: Feb 02, 2024 @ 4:00am ET
Intervals: 1
Ended: Feb 02, 2024 @ 4:11am ET      
"""
from sys import argv

def find_largest_power(n: int, p: int) -> int:
    x = 0

    while n:
        n /= p
        x += n
    
    return int(x)

if __name__ == '__main__':
    n = int(argv[1])
    p = int(argv[2])

    result = find_largest_power(n, p)
    print(result)