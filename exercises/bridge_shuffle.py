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
Ended: April 11, 2024 @ 7:05am ET
"""