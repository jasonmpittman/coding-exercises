__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Palindrome Descendent: 
A number may not be a palindrome, but its descendant can be. A number's direct child is created by summing each pair of adjacent digits to create the digits of the next number.

For instance, 123312 is not a palindrome, but its next child 363 is, where: 3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2.

Create a function that returns true if the number itself is a palindrome or any of its descendants down to the first 2 digit number (a 1-digit number is trivially a palindrome).

Examples

    palindromedescendant(11211230) ➞ true
    // 11211230 ➞ 2333 ➞ 56 ➞ 11

    palindromeDescendant(13001120) ➞ true
    // 13001120 ➞ 4022 ➞ 44

    palindromeDescendant(23336014) ➞ true
    // 23336014 ➞ 5665

    palindromeDescendant(11) ➞ true
    // Number itself is a palindrome.

Started: April 21, 2024 @ 5:55am ET
Intervals: 1
Ended: April 21, 2024 @ 6:25am ET
"""
