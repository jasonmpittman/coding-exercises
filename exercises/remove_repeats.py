__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that will remove any repeated character(s) in a word passed to the function. Not just consecutive characters, but characters repeating anywhere in the input.

Examples
    unrepeated("hello") ➞ "helo"
    unrepeated("aaaaa") ➞ "a"
    unrepeated("WWE!!!") ➞ "WE!"
    unrepeated("call 911") ➞ "cal 91"

Start: 05:55am
End: 06:03:am
Cycles: 1
"""
from sys import argv


def remove_repeats(word: str) -> str:
    new_word = ''

    for i in range(len(word)):
        if word[i] not in new_word:
            new_word = new_word + word[i]

    return new_word

if __name__ == "__main__":
    word = argv[1]

    result = remove_repeats(word)
    print(result)

