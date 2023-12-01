#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


""" Find Anagrams:

Write a function that finds all the start indices of anagrams of a given small string (p) in a bigger string (s). The order of output does not matter. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    findAllAnagrams("cbaebabacd", "abc") should return [0, 6] (the anagrams are at the start and near the end).
    findAllAnagrams("abab", "ab") should return [0, 1, 2] (multiple overlapping anagrams).
    findAllAnagrams("abcd", "e") should return [] (no anagrams present).

    cbaebabacd,abc
    abab,ab

Started: Dec 01, 2023 @ 5:00am ET
Intervals: 1
Ended: Dec 01, 2023 @ 5:30am ET 
"""

from itertools import permutations

def get_strings():
    s, p = input('Input s,p: ').split(',')

    return s.strip(), p.strip()


# TODO: bug: not handling overlapping correctly
def find_anagrams(s, p, anagrams):
    indices = []
    current_index = 0
    window_size = len(p)

    for i in range(0, len(s) - len(p)): # this should keep us from sliding too far right
        current_index = i
        window = s[i:i+window_size] # slice to get window

        if window in anagrams:
            indices.append(current_index)

    return indices


def permute_anagrams(p):
    anagrams = [''.join(i) for i in permutations(p)]

    return anagrams


if __name__ == '__main__':
    s, p = get_strings()
 
    anagrams = permute_anagrams(p)

    indices = find_anagrams(s, p, anagrams)
    print(indices)

    
    