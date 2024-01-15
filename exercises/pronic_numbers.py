__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Pronic Numbers:
A pronic number (or otherwise called as heteromecic) is a number which is a product of two consecutive integers, that is, a number of the form n(n + 1). Create a function that determines whether a number is pronic or not.

Examples:
    isHeteromecic(0) ➞ true
    // 0 * (0 + 1) = 0 * 1 = 0
    isHeteromecic(2) ➞ true
    // 1 * (1 + 1) = 1 * 2 = 2
    isHeteromecic(7) ➞ false
    isHeteromecic(110) ➞ true
    // 10 * (10 + 1) = 10 * 11 = 110
    isHeteromecic(136) ➞ false
    isHeteromecic(156) ➞ true

Started: Jan 15, 2024 @ 5:25am ET
Intervals: 1
Ended: Jan 15, 2024 @ 5:32am ET
"""
from sys import argv

def is_heteromecic(n: int) -> bool:
    
    for i in range(n):

        if i * (i + 1) == n:
            return True
        
    return False


if __name__ == '__main__':
    n = int(argv[1])

    result = is_heteromecic(n)
    print(result)