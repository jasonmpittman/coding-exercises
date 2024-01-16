__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Bigram Check:
You are given an input array of bigrams, and an array of words.

Write a function that returns true if every single bigram from this array can be found at least once in an array of words.

Examples:
    canFind(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ true

    canFind(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ false
    # "cu" does not exist in any of the words.

    canFind(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ true
    canFind(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ false

Started: Jan 16, 2024 @ 5:40am ET
Intervals: 1
Ended: Jan 16, 2024 @ 6:00am ET
"""
from sys import argv

def check_bigrams(bigrams : list, strings: list):
    match_map = {}

    for bigram in bigrams:
        for string in strings:    
            if bigram in string:
                match_map.update({bigram: 1})

    if len(bigrams) == len(match_map.keys()): # this feels hacky but it works
        return True
    else:
        return False             


if __name__ == '__main__':
    # at,be,th,au beautiful,the,hat -> true
    # ay,be,ta,cu maybe,beta,abet,course -> false
    # th,fo,ma,or the,many,for,forest -> true

    bigrams = argv[1].split(',')
    strings = argv[2].split(',')

    print(check_bigrams(bigrams, strings))
    