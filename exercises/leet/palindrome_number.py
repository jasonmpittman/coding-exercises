__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = "Easy"

"""
Given an integer x, return true if x is a, and false otherwise. 

Examples:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Start: 4:21am
End: 4:34am
"""
from sys import argv

def main(x: str) -> bool:
    is_palindrome = False

    digits = list(x)
    y = "".join(digits[::-1]) # use slicing to reverse list and then join to string

    if y == x:
        is_palindrome = True

    return is_palindrome

if __name__ == "__main__":
    x = argv[1]

    result = main(x)
    print(result)