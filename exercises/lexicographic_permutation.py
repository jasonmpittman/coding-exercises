__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Lexicographic Permutation:

A permutation is an ordered arrangement of objects. For exmaple, 3124 is one possible permutation of the digits 1,2,3, and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1, and 2 are:

012, 021, 102, 120, 201, 210

What is the millionth lexicographic permutation of the digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?


Started: Feb 15, 2024 @ 5:55am ET
Intervals: 1
Ended: Feb 15, 2024 @ 6:25am ET
"""
from itertools import permutations

def permute(digits):
    p = list(permutations(digits))
    print(p[999999])
    

# TODO: not returning a list of all permutations
def perms(digits, k = 0, p = []):
    
    if len(digits) == k:
        #print(digits)
        p.append(digits)
    else:
        for i in range(k, len(digits)):
            digits[k], digits[i] = digits[i], digits[k]
            perms(digits, k + 1, p)
            digits[k], digits[i] = digits[i], digits[k]
    
    return p



if __name__ == '__main__':
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # [0, 1, 2] # 
    p = perms(digits)
    print(p[999999])

    permute(digits)