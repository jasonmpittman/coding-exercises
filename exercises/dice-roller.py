#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Dice Roller: https://old.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/

Your input will contain one or more lines, where each line will be in the form of "NdM"; for example:
    3d6
    4d12
    1d10
    5d4

You should output the sum of all the rolls of that specified die, each on their own line. so if your input is "3d6", the output should look something like
    14

Bonus:
    14: 6 3 5
    
Started: Nov 26, 2023 @ 5:50am ET
Intervals: 1
Ended: Nov 26, 2023 @ 6:10am ET
"""

from random import randint

def get_dice_input():
    dice = []
    while True:
        die = input('Enter rolls one at a time: ')
        if die == 'q': break
        dice.append(die)

    return dice

def separate_dice(die): #internal utility function
    roll = die.split('d')

    return roll

def roll_dice(dice): #['3d6', '4d12']
    result = []
    
    #get roll from dice list
    for die in dice:
        total = 0
        #separate number of rolls from die type
        roll = separate_dice(die)

        #roll and print like total: roll1 roll2...rollN
        for i in range(int(roll[0])):
            total += randint(1, int(roll[1]))

        print(total)



if __name__ == '__main__':
    dice = get_dice_input()
    roll_dice(dice)
    