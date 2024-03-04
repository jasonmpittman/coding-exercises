__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" The Karaca's Encryption Algorithm:

Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"

Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Started: Mar 04, 2024 @ 7:00am ET
Intervals: 1
Ended: Marc 04, 2024 @ 7:25am ET
"""
from sys import argv

def reverse_plaintext(plaintext: str) -> str:
    return plaintext[::-1]

def replace_vowels(plaintext: str) -> str:
    vowels = ["o", "i", "u", "e", "a"]

    for vowel in vowels:
        if vowel in plaintext and vowel == "a":
            plaintext = plaintext.replace(vowel, "0")
        elif vowel in plaintext and vowel == "e":
            plaintext = plaintext.replace(vowel, "1")
        elif vowel in plaintext and vowel == "i":
            plaintext = plaintext.replace(vowel, "2")
        elif vowel in plaintext and vowel == "o":
            plaintext = plaintext.replace(vowel, "2")
        elif vowel in plaintext and vowel == "u":
            plaintext = plaintext.replace(vowel, "3")

    return plaintext

def append(plaintext: str) -> str:
    return plaintext + "aca"

def encipher(plaintext: str) -> str:
    ciphertext = ''

    reversed_plaintext = reverse_plaintext(plaintext)

    zeroed_plaintext = replace_vowels(reversed_plaintext)

    ciphertext = append(zeroed_plaintext)

    return ciphertext


if __name__ == "__main__":
    plaintext = argv[1]

    ciphertext = encipher(plaintext)
    print(ciphertext)