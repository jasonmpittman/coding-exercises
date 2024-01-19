__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" First Letter:
Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).

Examples:
    shift_sentence("create a function") ➞ "freate c aunction"
    shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"
    shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"
    shift_sentence("edabit") ➞ "edabit"

Notes:
    The last word shifts its first letter to the first word in the sentence.
    All sentences will be given in lowercase.
    Note how single words remain untouched (example #4).

Started: Jan 19, 2024 @ 6:15am ET
Intervals: 1
Ended: Jan 19, 2024 @ 6:45am ET
"""
from sys import argv

def shift_first_letters(sentence: list) -> str:
    first_letters = []
    pointer = 0
    new_sentence = []
    sentence_length = len(sentence)

    for word in sentence:
        first_letters.append(word[0])

    # TODO: could refactor the letter switching to another function
    for i in range(sentence_length):
        # this handles the shift of the last word first letter to the first word first letter
        if i == sentence_length - 1:
            word = list(sentence[0])
            word[0] = first_letters[-1]
            new_word = "".join(word)
            
            new_sentence.insert(0, new_word)
        elif i < sentence_length:
            word = list(sentence[i + 1])
            word[0] = first_letters[i]
            new_word = "".join(word)
            
            new_sentence.append(new_word)

    return new_sentence

if __name__ == '__main__':
    sentence = argv[1].split(' ')
    
    if len(sentence) <= 1:
        print(sentence)
    else:
        print(shift_first_letters(sentence))