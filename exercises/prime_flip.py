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