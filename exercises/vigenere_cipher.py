__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a class that, when given a key and an alphabet, can be used to encode and decode from a Vigenere cipher.
Examples

alphabet = "abcdefghijklmnopqrstuvwxyz"
key      = "password"

"codewars" --> encode -->  "rovwsoiv"
"laxxhsj"  --> decode -->  "waffles"

Note: any character not in the alphabet must be left alone. For example in the above case:

"CODEWARS"  --> encode -->  "CODEWARS"


Start: 07:05pm
End: 07:33pm
Cycles: 1
"""
from sys import argv

def encipher(plaintext: str, key: str) -> str:
    """ implementation of Ei = (Pi + Ki) mod 26 """
    ciphertext = []

    for i in range(len(plaintext)):
        letter = plaintext[i]

        if letter != ' ':
            enciphered_letter = chr( (ord(letter) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            enciphered_letter = ' '
        
        ciphertext.append(enciphered_letter)

    return "".join(ciphertext)

def decipher(ciphertext: str, key: str) -> str:
    """ implementation of Di = (Ei - Ki) mod 26 """
    plaintext = []

    for i in range(len(ciphertext)):
        letter = ciphertext[i]

        if letter != ' ':
            plaintext_letter = chr( (ord(letter) - ord(key[i]) + 26 ) % 26 + ord('a'))
        else:
            plaintext_letter = ' '
        
        plaintext.append(plaintext_letter)

    return "".join(plaintext)



if __name__ == "__main__":
    text = argv[1]
    key = argv[2]
    option = argv[3]

    if option == "e":
        result = encipher(text, key)
        print(result)
    
    if option == "d":
        result = decipher(text, key)
        print(result)

    if option == '' or option == None:
        print("Please provide a valid operation option")

