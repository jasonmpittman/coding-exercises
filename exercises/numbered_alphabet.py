__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Numbered Alphabet:
Create a function that converts a string of letters to their respective number in the alphabet.

Examples:
    alphNum("XYZ") ➞ "23 24 25"
    alphNum("ABCDEF") ➞ "0 1 2 3 4 5"
    alphNum("JAVASCRIPT") ➞ "9 0 21 0 18 2 17 8 15 19"

Started: Mar 11, 2024 @ 6:00pm ET
Intervals: 1
Ended: March 11, 2024 @ 6:07pm ET
"""
from sys import argv


def number_alphabet(plaintext: str) -> list:
    ciphertext = ""
    
    # didn't feel like hardcoding a dictionary
    letters = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = {letter:str(num) for (num,letter) in enumerate(letters.upper()) }

    for char in plaintext:
        ciphertext += alphabet[char] + ' '

    return ciphertext

if __name__ == "__main__":
    plaintext = argv[1].upper()

    ciphertext = number_alphabet(plaintext)
    print(ciphertext)