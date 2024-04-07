__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Zygodromes:
A number is Zygodrome if it can be partitioned into clusters of repeating digits with a length equals or greater than two (as to say that repeating digits need to be placed as an adjacent pair or a greater group, and that no single digits are allowed).

Given a non-negative integer num, implement a function that returns true if num is a Zygodrome number, or false otherwise.

Examples:
    isZygodrome(11) ➞ true
    // 11 is a pair of repeated digits
    isZygodrome(33322) ➞ true
    // 333 is a triplet of repeated digits, and 22 is a pair
    isZygodrome(5) ➞ false
    // 5 is a single digit, it doesn't form a pair
    isZygodrome(1001) ➞ false
    // 00 is a pair, but the two 1's are not adjacent

Started: April 07, 2024 @ 7:20am ET
Intervals: 1
Ended: April 07, 2024 @ 7:50am ET
"""