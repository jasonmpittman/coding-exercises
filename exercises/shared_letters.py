__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Shared Letters:
Create a function that returns the number of characters shared between two words.

Examples
    sharedLetters("apple", "meaty") ➞ 2
    // Since "ea" is shared between "apple" and "meaty".

    sharedLetters("fan", "forsook") ➞ 1

    sharedLetters("spout", "shout") ➞ 4

Started: May 31, 2024 @ 7:15am ET
Intervals: 1
Ended: May 31, 2024 @ 7:19am ET
"""
from sys import argv

def count_shared_letters(A: str, B: str) -> int:
    count = 0

    for a in A:
        if a in B:
            count += 1

    return count

if __name__ == "__main__":
    A = argv[1]
    B = argv[2]

    count = count_shared_letters(A, B) # apple meaty
    print(count)
