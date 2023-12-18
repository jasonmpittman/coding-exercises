__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Coin Flips:

Alice and Bob have each picked a string containing only heads and tails. Then a fair coin is flipped until a sequence of consecutive flips matches one or both of the strings. Alice wins if her string appears first, and Bob wins if his appears first. It's possible that both of their strings appear at the same time. In that case the game is a tie.

Given the two strings, what is the probability of these three outcomes?

Input
    The first line of input is Alice's string, and the second line is Bob's. These strings contain only Hs and Ts, and their lengths are between 1 and 20, inclusive.

Output
    The output consists of three lines, each of which contains a single real number. They should be the probability that Alice wins, the probability that Bob wins, and the probability of a tie.

H
T

0.500000000000
0.500000000000
0.000000000000

HHT
HTH

0.666666666667
0.333333333333
0.000000000000

Started: Dec 18, 2023 @ 4:30am ET
Intervals: 1
Ended: Dec 18, 2023 @ 5:00am ET 
"""

from sys import argv


if __name__ == '__main__':
    alice = argv[1]
    bob = argv[2]