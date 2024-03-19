__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Shared Digits:
Create a function that returns true if each pair of adjacent numbers in an array shares at least one digit and false otherwise.

Examples

    sharedDigits([33, 53, 6351, 12, 2242, 44]) ➞ true
    // 33 and 53 share 3, 53 and 6351 share 3 and 5, etc.
    sharedDigits([1, 11, 12, 13, 14, 15, 16]) ➞ true
    sharedDigits([33, 44, 55, 66, 77]) ➞ false
    sharedDigits([1, 12, 123, 1234, 1235, 6789]) ➞ false

Started: Mar 18, 2024 @ 6:00am ET
Intervals: 1
Ended: March 18, 2024 @ 6:25am ET
"""

from sys import argv


def is_number_shared(n: str, m: str) -> bool:
    shared = False

    for i in [*n]:
        shared = True if i in [*m] else False
        if shared == True:
            break

    return shared

def are_digits_shared(array: list) -> bool:
    l = len(array)
    shared = False
    i = 0
    j = 1

    while j < l:
        print("Comparing {} and {}".format(array[i], array[j]))
        shared = is_number_shared(array[i], array[j])
        
        i += 1
        j += 1
    
    return shared

    

if __name__ == "__main__":
    array = argv[1].split(',') # 1,11,12,13,14,15,16  33,44,55,66,77  33,53,6351,12,2242,44
    print(are_digits_shared(array))