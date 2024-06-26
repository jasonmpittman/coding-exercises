__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Counting Duplicates:
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

Started: May 22, 2024 @ 6:35am ET
Intervals: 1
Ended: May 22, 2024 @ 6:38am
"""
from sys import argv

def count_duplicates(string: str) -> int:
    duplicates = {}

    for s in string:
        if string.count(s) > 1 and s not in duplicates:
            count = string.count(s)
            duplicates[s] = count

    return duplicates


if __name__ == "__main__":
    string = argv[1].lower()

    duplicates = count_duplicates(string)
    print(duplicates)