__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Substring Count:
Complete the solution so that it returns the number of times the search_text is found within the full_text. Overlap is not permitted : "aaa" contains 1 instance of "aa", not 2.

Usage example:

full_text = "aa_bb_cc_dd_bb_e", search_text = "bb"
    ---> should return 2 since "bb" shows up twice


full_text = "aaabbbcccc", search_text = "bbb"
    ---> should return 1

Started: Mar 8th, 2025 @ 9:05am ET (estimated)
Intervals: 1
Ended: Mar 8th, 2025 @ 9:10am ET
"""
import sys

def count_substring(string: str, substring: str) -> int:
    count = string.count(substring)

    return count


if __name__ == "__main__":
    string = sys.argv[1]
    substring = sys.argv[2]

    count = count_substring(string, substring)
    print(count)