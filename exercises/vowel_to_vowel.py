__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
Examples

vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False

Start: 06:50am
End: 07:00:am
Cycles: 1
"""
from sys import argv

def is_vowel_to_vowel(sentence: str) -> bool:
    words = sentence.split(' ')
    is_vowel_link = False
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(words) - 1):
        last_letter = words[i][len(words[i]) - 1] # last letter of current word
        first_letter = words[i + 1][0] # first letter of next word

        if last_letter in vowels and first_letter in vowels:
            is_vowel_link = True

    return is_vowel_link

if __name__ == "__main__":
    sentence = argv[1]

    result = is_vowel_to_vowel(sentence)
    print(result)

