__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Bridge Shuffle:
Create a function to bridge shuffle two arrays. To bridge shuffle, you interleave the elements from both arrays in an alternating fashion, like so:

Array 1 = ["A", "A", "A"]
Array 2 = ["B", "B", "B"]

Shuffled Array = ["A", "B", "A", "B", "A", "B"]

Examples:
    bridgeShuffle(["A", "A", "A"], ["B", "B", "B"]) ➞ ["A", "B", "A", "B", "A", "B"]
    bridgeShuffle(["C", "C", "C", "C"], ["D"]) ➞ ["C", "D", "C", "C", "C"]
    bridgeShuffle([1, 3, 5, 7], [2, 4, 6]) ➞ [1, 2, 3, 4, 5, 6, 7]

Started: April 11, 2024 @ 6:35am ET
Intervals: 1
Ended: April 11, 2024 @ 7:00am ET
"""
from sys import argv
from itertools import zip_longest


def bridge_shuffle(array_1: list, array_2: list) -> list:
    #return [j for i in zip(array_1, array_2) for j in i] # here zip is limited to shortest array
    return [j for i in zip_longest(array_1, array_2) for j in i] # we get a None padded but we could remove it with extra code


if __name__ == "__main__":
    array_1 = argv[1].split(',') # a,a,a b,b,b
    array_2 = argv[2].split(',')

    shuffled_array = bridge_shuffle(array_1, array_2)
    print(shuffled_array)