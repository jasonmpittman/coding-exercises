__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Paired Numbers:

Write a function that pairs the first number in an array with the last, the second number with the second to last, etc.
    Examples

    pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]

    pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]

    pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]

    pairs([]) ➞ []

Notes

    If the list has an odd length, repeat the middle element twice for the last pair.
    Return an empty list if the input is an empty list.
    
Started: Feb 06, 2025 @ 5:25am ET
Intervals: 1
Ended: Feb 06, 2025 @ 6:03am ET
"""

def extract_pair(pairs: list, i: int) -> list:
    pair = []

    pair.append([pairs[i], pairs[-1 + (-i)]])

    return pair

def pair_numbers(pairs: list) -> list:
    paired_numbers = []
    pairs_length = len(pairs)

    for i in range(0, int((pairs_length / 2))):
        paired_numbers.append(extract_pair(pairs, i))

    if pairs_length % 2 != 0:
        middle_pair = [pairs[ int(pairs_length / 2) ],
                       pairs[ int(pairs_length / 2) ]
                       ]
        paired_numbers.append(middle_pair)

    print(paired_numbers)

    return paired_numbers

if __name__ == "__main__":
    #pairs = [1,2,3,4,5,6]
    pairs = [5,9,8,1,2]

    pair_numbers(pairs)
