__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Prime Flip:
A prime number is a number whose only proper (non-self) divisor is 1 (example 13).

An emirp (prime spelled backwards) is a non-palindromic prime which, when its digits are reversed, makes another prime. E.g. 13 is a prime, and so is 31. Both are therefore emirps.

A bemirp is a prime which is an emirp (makes another prime with its digits reversed), but additionally, makes another prime when flipped upside down (see note). The upside-down version is also an emirp, which makes a group of 4 primes. Bemirps consist only of digits 0, 1, 6, 8, and 9.

To illustrate: 11061811, reversed = 11816011, upside-down = 11091811, upside-down reversed = 11819011. All four are primes.

Create a function that takes a number and returns "B" if it’s a bemirp, "E" if it's a (non-bemirp) emirp, "P" if it's a (non-emirp) prime, or "C" (composite / non-prime).

Examples
    bemirp(101) ➞ "P"
    bemirp(1011) ➞ "C"
    bemirp(1069) ➞ "E"
    bemirp(1061) ➞ "B"

Started: Mar 31, 2024 @ 5:25am ET
Intervals: 1
Ended: March 31, 2024 @ 5:55am ET
"""
from sys import argv

def is_prime(n: int) -> bool:
    if n > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (n//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def is_emirp(n: int) -> bool:
    # do i need to check n is not palindromatic?
    if len(str(n)) > 1 and is_prime(int(str(n)[::-1])):
        return True
    else:
        return False

def is_bemirp(n: int) -> bool:
    str_n = str(n)
    
    if '6' in str_n:
        bemirp = str_n.replace('6', '9')

    if is_emirp(int(bemirp)) and is_prime(int(bemirp)):
        return True
    else:
        return False

def flip_prime(n: int) -> str:
    if is_prime(n) == False:
        print("C")
    elif is_prime(n) and is_emirp(n) and is_bemirp(n):
        print("B")
    elif is_prime(n) and is_emirp(n) and not is_bemirp(n): 
        print("E")
    elif is_prime(n) and not is_emirp(n) and not is_bemirp(n): 
        print("P")
    
 

if __name__ == "__main__":
    n = argv[1]

    flip_prime(int(n))