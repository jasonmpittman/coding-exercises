__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = "Medium"

"""
Given a string s, find the length of the longest without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Start: 12:28pm
End: 12:49pm
"""
from sys import argv

def main(s: str) -> int:
    string_length = len(s)
    sub = ''

    for c in s:
        if c not in sub:
            sub = sub + c
    
    return len(sub)


if __name__ == "__main__":
    s = argv[1]

    result = main(s)
    print(result)