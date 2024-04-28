__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" First Occurrence:
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

<forgot to commit yesterday 4/28>
Started: April 27, 2024 @ 4:45am ET
Intervals: 1
Ended: April 27, 2024 @ 5:15am ET
"""
from sys import argv

def find_first_occurrence(haystack: str, need: str) -> int:

    try:
        index = haystack.index(needle)
    except ValueError:
        return -1

    return index

if __name__ == "__main__":
    haystack = argv[1] # sadbutsad sad
    needle = argv[2]

    print(find_first_occurrence(haystack, needle))