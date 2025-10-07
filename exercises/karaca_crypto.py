__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Make a function that encrypts a given input with these steps:

Input: "apple"
Step 1: Reverse the input: "elppa"
Step 2: Replace all vowels using the following chart:
    a  0
    e  1
    i  2
    o  2
    u  3

# "1lpp0"

Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"
Examples
    encrypt("banana") ➞ "0n0n0baca"
    encrypt("karaca") ➞ "0c0r0kaca"
    encrypt("burak") ➞ "k0r3baca"
    encrypt("alpaca") ➞ "0c0pl0aca"

Start: 04:10am
End: 04:26:am
Cycles: 1
"""
from sys import argv
from enum import Enum

def reverse_string(string: str) -> str:
    return string[::-1]

def encipher(plaintext: str) -> str:
    ciphertext = ''
    append = 'aca'
    vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

    plaintext = reverse_string(plaintext)

    for letter in plaintext:
        if letter in vowels:
            ciphertext += str(vowels[letter])
        else:
            ciphertext += letter
    
    ciphertext += append

    return ciphertext


if __name__ == "__main__":
    plaintext = argv[1]

    ciphertext = encipher(plaintext)
    print(ciphertext)


