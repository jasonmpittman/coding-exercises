__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = "Easy"

""" 
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

Constraints:

    1 <= s.length <= 105
    s consists only of lowercase English letters.

"""
import re

def remove_character(s: str, c: str) -> str:
    """ Remove a character and return the new string """
    s = s.replace(c, "", 1)

    return s

def main(s: str) -> str:
    for c in s:
        print(f"Checking {c} in {s}")
        if s.count(c) >= 3: #   need consecutive test here...leeetcode goes to letcode
            print(f"{c} occurs 3 or more times in {s}")
            s = remove_character(s, c)
            print(f"New string is {s}")



if __name__ == "__main__":
    s = "leeetcode"
    main(s)