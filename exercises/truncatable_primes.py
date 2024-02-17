__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Truncatable Primes:
A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

    If the integer is only a left-truncatable prime, return "left".
    If the integer is only a right-truncatable prime, return "right".
    If the integer is both, return "both".
    Otherwise, return False.

Examples:
    truncatable(9137) ➞ "left"
    # Because 9137, 137, 37 and 7 are all prime.

    truncatable(5939) ➞ "right"
    # Because 5939, 593, 59 and 5 are all prime.

    truncatable(317) ➞ "both"
    # Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.


Started: Feb 17, 2024 @ 5:00am ET
Intervals: 1
Ended: Feb 17, 2024 @ 5:30am ET
"""
from sys import argv

def is_prime(n: int) -> bool:
    print(n)
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
                break
        else:
            return True
    else:
        return False

# TODO: from right to left is broken
def is_truncatable(n: str) -> str:
    left = False
    right = False
    m = n
    # test if 0 present
    if '0' in n:
        return False, False
    
    # test if prime from left to right
    while n:
        if is_prime(int(n)):
            n = n[1:]
            if len(n) >= 1:
                left = is_prime(int(n))        
        else:
            False

    # test if prime from right to left
    #while m:
    #    if is_prime(int(m)):
    #        m = m[:-1]
    #        if len(m) >= 1:
    #            right = is_prime(int(m))        
    #    else:
    #        False


    return left, right

if __name__ == "__main__":
    n = argv[1]

    left, right = is_truncatable(n)

    if left and right:
        print("Both")
    elif left and not right:
        print("Left")
    elif not left and right:
        print("Right")
    else:
        print("False")