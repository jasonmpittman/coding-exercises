__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Pangrams:
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.


Started: June 11, 2024 @ 5:35am ET
Intervals: 1
Ended: June 11, 2024 @ 5:47am ET
"""
import string
from sys import argv


def is_pangram(sentence: str) -> bool:
    # build a dictionary of lowercase letters as keys and 0 as value for each
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    
    for letter in sentence:
        if letter != " " or letter.isdigit == False:
            alphabet[letter.lower()] += 1

    # all is true when every value in dictionary is > 0 else false
    return all(value > 0 for value in alphabet.values())


if __name__ == "__main__":
    sentence = argv[1]

    result = is_pangram(sentence)
    print(result)