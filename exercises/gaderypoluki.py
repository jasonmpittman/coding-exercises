__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Gaderypoluki Cipher: https://edabit.com/challenge/y5hDyugNk5A9KRbLc

Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:

"gaderypoluki" -> "ga de ry po lu ki"

Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character in the grouped version of the key. If the message character does not appear in the key, leave it as is. If the letter in the key occurs more than once, the first result is used. Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:

"gaderypoluki" -> "ga de ry po lu ki"

Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character in the grouped version of the key. If the message character does not appear in the key, leave it as is. If the letter in the key occurs more than once, the first result is used. For example: use the above key, if the letter "a" appeared in the message, it would be replaced with "g" since "g" in the adjacent letter.

Return the encrypted message.

Started: Feb 09, 2024 @ 7:10am ET
Intervals: 1
Ended: Feb 09, 2024 @ 7:40am ET
"""
from sys import argv

def transform_key(key: str) -> str:
    step = 2
    transformed_key = ''
    key = [c for c in key]
    
    for i in range(len(key) - 1):
        transformed_key += str(key[i:step])
        
        i += 1
        step += 1

    return transformed_key

#TODO: need to fix line 50 so that the right char is replaced
def encrypt(key: str, message: str) -> str:
    encrypted_message = message

    key = transform_key(key)
    
    for c in message:
        if c in key:
            encrypted_message = encrypted_message.replace(c, key[key.index(c) - 1], -1)

    return encrypted_message

if __name__ == '__main__':
    key = argv[1] # gaderypoluki "This is an encrypted message"
    message = argv[2]

    encryptoed_message = encrypt(key, message)
    print(encryptoed_message)