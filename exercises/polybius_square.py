__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Polybius Square:
The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).

To encipher a message, each letter is merely replaced by its row and column numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.

Examples:
    polybius("Hi") ➞ "2324"
    polybius("2324  4423154215") ➞ "hi there"
    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

Started: Mar 26, 2024 @ 4:45am ET
Intervals: 1
Ended: March 26, 2024 @ 5:15am ET
"""
from sys import argv
from enum import Enum

# polybius square data structure
polybius = {
    1: {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"},
    2: {1: "f", 2: "g", 3: "h", 4: "i", 5: "k"},
    3: {1: "l", 2: "m", 3: "n", 4: "o", 5: "p"},
    4: {1: "q", 2: "r", 3: "s", 4: "t", 5: "u"},
    5: {1: "v", 2: "w", 3: "x", 4: "y", 5: "z"}
}

def get_keys_by_value(dictionary, value):
    keys = []
    for outer_key, inner_dict in dictionary.items():
        for inner_key, inner_value in inner_dict.items():
            if inner_value == value:
                keys.append((outer_key, inner_key))
    return keys

def get_values_by_keys(dictionary, keys):
    values = []
    for outer_key, inner_dict in dictionary.items():
        for inner_key, inner_value in inner_dict.items():
            if (outer_key, inner_key) in keys:
                values.append(inner_value)
    return values

# TODO: returns list of tuples and we want a string
def encipher(plaintext: str) -> str:
    ciphertext = []
    #get coordinates for each char in string
    for char in plaintext:
        ciphertext.append(get_keys_by_value(polybius, char))
    
    print(ciphertext)

# TODO: not working - get TypeError on 68
def decipher(ciphertext: str) -> str:
    plaintext = []

    for i in range(0, len(ciphertext), 2):
        block = ciphertext[:2]
        plaintext.append(get_values_by_keys(polybius, block))
        ciphertext = ciphertext.replace(block, '', 1)
    
    print(plaintext)

if __name__ == "__main__":
    string = argv[1]

    if any(char.isdigit() for char in string): # neat use of any() against a list comprehension
        decipher(string.lower())
    else:
        encipher(string.lower())