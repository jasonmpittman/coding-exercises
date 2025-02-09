__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Bird Codes:

In the world of birding there are four-letter codes for the common names of birds. These codes are created by some simple rules:

    If the bird's name has only one word, the code takes the first four letters of that word.
    If the name is made up of two words, the code takes the first two letters of each word.
    If the name is made up of three words, the code is created by taking the first letter from the first two words and the first two letters from the third word.
    If the name is four words long, the code uses the first letter from all the words.

There are other ways codes are created, but this challenge will only use the four rules listed above.

In this challenge you will write a function that takes a list of strings of common bird names and create the codes for those names based on the rules above. The function will return a list of codes in the same order in which the input names were presented.
    Examples

    bird_code(["Black-Capped Chickadee", "Common Tern"]) ➞ ["BCCH", "COTE"]

    bird_code(["American Redstart", "Northern Cardinal"]) ➞ ["AMRE","NOCA"]

    bird_code(["Bobolink", "American White Pelican"]) ➞ ["BOBO","AWPE"]


Started: Feb 10, 2025 @ 5:40am ET
Intervals: 1
Ended: Feb 10, 2025 @ 6:10am ET
"""
# TODO: finish handling - in names
def build_bird_code(bird_names):
    codes = []

    for name in bird_names:
        words = name.split(' ')

        # handle hyphenated words
        for word in words:
            clean_word = word.replace('-', ' ')
            i = words.index(word)
            words[i] = clean_word

        # if one word in name
        if len(words) == 1:
            codes.append(words[0][:4].upper())
        
        # if two words in name
        if len(words) == 2:
            codes.append(words[0][:2].upper() + words[1][:2].upper())

        # if three words in name
        if len(words) == 3:
            codes.append(words[0][:1].upper() + words[1][:1].upper() + words[2][:2].upper())
    
    return codes

if __name__ == "__main__":
    bird_names = ["Black-Capped Chickadee", "Common Tern"]

    codes = build_bird_code(bird_names)
    print(codes)
