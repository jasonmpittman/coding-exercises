__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" String Pairs:

Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.

Examples:

    string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]
    string_pairs("edabit") ➞ ["ed", "ab", "it"]
    string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]

Started: Dec 30, 2023 @ 5:50am ET
Intervals: 1
Ended: Dec 30, 2023 @ 6:18am ET
"""
from sys import argv

def get_string_pairs(s):
    pairs = []
    window = 0

    # TODO: this could be refactored
    if len(s) % 2 == 0:
        for i in range(len(s) // 2):
            pair = s[window:(window + 2)]
            pairs.append(pair)
            window += 2
    else:
        for i in range((len(s) // 2) + 1):
            pair = s[window:(window + 2)]
            
            if len(pair) == 1:  
                pair = pair + '*'

            pairs.append(pair)
            window += 2

    return pairs

if __name__ == '__main__':
    s = argv[1]

    print(get_string_pairs(s))