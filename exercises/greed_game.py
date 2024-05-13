__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Greed Game:
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)


Started: May 13, 2024 @ 7:30am ET
Intervals: 1
Ended: May 13, 2024 @ 7:45am
"""
from sys import argv

def score_dice(dice: list) -> int:
    score = 0

    if dice.count('1') >= 3:
        score += 1000

        for _ in range(3):
            dice.remove('1')
    
    if dice.count('6') >= 3:
        score += 600
        
        for _ in range(3):
            dice.remove('6')

    if dice.count('5') >= 3:
        score += 500
                
        for _ in range(3):
            dice.remove('5')
    
    if dice.count('4') >= 3:
        score += 400

        for _ in range(3):
            dice.remove('4')

    if dice.count('3') >= 3:
        score += 300

        for _ in range(3):
            dice.remove('3')
    
    if dice.count('2') >= 3:
        score += 200

        for _ in range(3):
            dice.remove('2')
    
    if dice.count('1') <= 2:
        score += 100 * dice.count('1')
    
    if dice.count('5') <= 2:
        score += 50 * dice.count('5')

    return score

if __name__ == "__main__":
    dice = argv[1].split(',')

    score = score_dice(dice) # 5,1,3,4,1
    print(score)