__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Generala:

Generala is a dice game popular in South America. It's very similar to Yahtzee but with a different scoring approach. It is played with 5 dice, and the possible results are:
Result 	Points 	Rules 	Samples
GENERALA 	50 	When all rolled dice are of the same value. 	66666, 55555, 44444, 11111, 22222, 33333.
POKER 	40 	Four rolled dice are of the same value. 	44441, 33233, 22262.
FULLHOUSE 	30 	Three rolled dice are of the same value, the remaining two are of a different value, but equal among themselves. 	12121, 44455, 66116.
STRAIGHT 	20 	Rolled dice are in sequential order. Dice with value 1 is a wildcard that can be used at the beginning of the straight before a 2, or at the end of it after a 6. 	12345, 23456, 34561, 13654, 62534.
Anything else 	0 	Anything else will return 0 points. 	44421, 61623, 12346.

Please note that dice are not in order; for example 12543 qualifies as a STRAIGHT. Also, No matter what string value you get for the dice, you can always reorder them any order you need to make them qualify as a STRAIGHT. I.E. 12453, 16543, 15364, 62345 all qualify as valid STRAIGHTs.

Complete the function that is given the rolled dice as a string of length 5 and return the points scored in that roll. You can safely assume that provided parameters will be valid:

    String of length 5,
    Each character will be a number between 1 and 6


Started: Feb 11, 2025 @ 3:20am ET
Intervals: 1
Ended: Feb 11, 2025 @ 3:50am ET
"""

import random

def roll_dice() -> list:
    dice = []

    for i in range(5):
        dice.append(random.randrange(1, 6))

    return dice

# TODO: implement full house logic
def score_dice(rolled_dice: list) -> int:
    rolled_dice.sort()

    for die in rolled_dice:
        # all same number
        if rolled_dice.count(rolled_dice[die]) == len(rolled_dice):
            return 50

        # four same number
        elif rolled_dice.count(rolled_dice[die]) == 4:
            return 40
        
        # full house

        # straight sequence
        s = "".join(str(i) for i in rolled_dice)
        if any(sublist in s for sublist in ('12345', '23456', '34561', '13654', '62534')):
            return 20 

        # else zero
        else:
            return 0


if __name__ == "__main__":
    rolled_dice = roll_dice()
    print(rolled_dice)

    score = score_dice(rolled_dice)
    print(score)
