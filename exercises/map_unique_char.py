
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function that returns a character mapping from a word.

Examples:
    character_mapping("abcd") ➞ [0, 1, 2, 3]
    character_mapping("abb") ➞ [0, 1, 1]
    character_mapping("babbcb") ➞ [0, 1, 0, 0, 2, 0]
    character_mapping("hmmmmm") ➞ [0, 1, 1, 1, 1, 1]

Start: 6:25am
End: 6:51:am
Cycles: 1
"""
from sys import argv

def create_map(word: list) -> list:
    char_map = {}
    values = []
    index = 0

    for character in word:
        if character in char_map.keys():
            print(f'{character} is in our char_map.')
            print(f'value of {character} is {char_map[character]}.')
            values.append(char_map[character])
        else:
            print(f'{character} not in our char_map')
            char_map[character] = index
            values.append(index)
            index += 1
            
    return values

if __name__ == "__main__":
    word = list(argv[1])

    values = create_map(word)
    print(values)

