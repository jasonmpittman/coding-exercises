__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Word Salad:
Slice each word in half and sort the chunks alphabetically. This recipe tastes best when the chunks are joined together to make a string.

Examples:
    fruitSalad(["apple", "pear", "grapes"]) ➞ "apargrapepesple"
    fruitSalad(["raspberries", "mango"]) ➞ "erriesmangoraspb"
    fruitSalad(["banana"]) ➞ "anaban"

Started: Mar 21, 2024 @ 5:45am ET
Intervals: 1
Ended: March 21, 2024 @ 5:56am ET
"""
from sys import argv


def mix_salad(strings: str) -> list:
    chunks = []

    # create chunks
    for s in strings:
        length = len(s)
        chunks.append(s[:length // 2])
        chunks.append(s[length // 2:])

    # sort the chunks
    mixed_strings = sorted(chunks)

    return ''.join(mixed_strings)

if __name__ == "__main__":
    strings = argv[1].split(',') # apple,pear,grapes

    mixed_strings = mix_salad(strings)
    print(mixed_strings)