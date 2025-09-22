__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
write a function that pairs the first number in an array with the last, the second number with the second to last, etc.

Examples
    pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
    pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]
    pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]
    pairs([]) ➞ []

Start: 5:55am
End: 6:08:am
Cycles: 1
"""
from sys import argv

def get_pair(array: list, n: int, m: int) -> list:
    pair = [array[n], array[m]]

    return pair

if __name__ == "__main__":
    array = argv[1].split(',')
    n = 0
    m = len(array) - 1
    pairs = []

    while n <= m:
        pair = get_pair(array, n, m)
        pairs.append(pair)
        n += 1
        m -= 1    

    print(pairs)