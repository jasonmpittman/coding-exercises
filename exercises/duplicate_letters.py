__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.

Examples
    no_duplicate_letters("Fortune favours the bold.") ➞ True
    no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
    no_duplicate_letters("Look before you leap.") ➞ False
    # Duplicate letters in "Look" and "before".
    no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
    # Duplicate letters in "apple", "keeps", "doctor", and "away".

Start: 7:10am
End: 7:18:am
Cycles: 1
"""
from sys import argv

def has_duplicate_letters(sentence: str) -> bool:
    has_duplicate = True

    words = sentence.split(' ')
    
    for word in words:
        if len(word) != len(set(word)):
            has_duplicate = False

    return has_duplicate

if __name__ == "__main__":
    sentence = argv[1]

    result = has_duplicate_letters(sentence)
    print(result)
