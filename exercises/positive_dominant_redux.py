__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Positive Dominant:

An array is positive dominant if it contains strictly more unique positive values than unique negative values. Write a function that returns true if an array is positive dominant.

Examples:
    isPositiveDominant([1, 1, 1, 1, -3, -4]) ➞ false
    // There is only 1 unique positive value (1).
    // There are 2 unique negative values (-3, -4).

    isPositiveDominant([5, 99, 832, -3, -4]) ➞ true
    isPositiveDominant([5, 0]) ➞ true
    isPositiveDominant([0, -4, -1]) ➞ false

Started: Feb 02, 2024 @ 4:15am ET
Intervals: 1
Ended: Feb 02, 2024 @ 4:25am ET     
"""
from sys import argv

def is_positive_dominant(my_list: list) -> bool:
    negatives = 0
    positives = 0

    # let's use a lambda function to test for the negative symbol on n as a str
    for n in my_list:
        is_negative = lambda n: str(n)[0] == '-' and len(str(n))>1
        
        if is_negative(n):
            negatives += 1
        else:
            positives += 1
    
    if positives > negatives:
        return True
    else:
        return False

if __name__ == '__main__':
    my_list = argv[1].split(',') # 1,1,1,1,-3,-4 or 0,-4,-1
    print(is_positive_dominant(my_list))