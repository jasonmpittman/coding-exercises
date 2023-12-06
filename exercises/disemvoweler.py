#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


"""Disemvoweler: https://old.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/

A string consisting of a series of words to disemvowel. It will be all lowercase (letters a-z) and without punctuation. The only special character you need to handle is spaces.

    Sample Input 1

    all those who believe in psychokinesis raise my hand

    Sample Output 1

    llthswhblvnpsychknssrsmyhnd
    aoeoeieeioieiaiea


Started: Dec 06, 2023 @ 5:30am ET
Intervals: 1
Ended: Dec 06, 2023 @ 6:00am ET
"""

def disemvowel_brute(vowels, text):
    disemvoweled = text
    string = text

    for character in disemvoweled:
        if character not in vowels:
            disemvoweled = disemvoweled.replace(character, '')
        
    for character in string:
        if character in vowels:
            string = string.replace(character, '')

    print(string)
    print(disemvoweled)

def disemvowel(vowels, text):
    disemvoweled = "".join(character for character in text if character in vowels)
    string = "".join(character for character in text if character not in vowels)

    print(string)
    print(disemvoweled)
    

if __name__ == '__main__':
    vowels = list('aeiou')
    text = input('Enter string to disemvowel: ').replace(' ', '')

    disemvowel(vowels, text)
    disemvowel_brute(vowels, text)

    