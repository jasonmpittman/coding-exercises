#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Monty Hall Problem: https://old.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/

The Monty Hall scenario goes like this:

    There are three closed doors, labeled #1, #2, and #3. Monty Hall randomly selects one of the three doors and puts a prize behind it. The other two doors hide nothing.

    A contestant, who does not know where the prize is, selects one of the three doors. This door is not opened yet.
    
    Monty chooses one of the three doors and opens it. The door that Monty opens (a) does not hide the prize, and (b) is not the door that the contestant selected. There may be one or two such doors. If there are two, Monty randomly selects one or the other.
    
    There are now two closed doors, the one the contestant selected in step 2, and one they didn't select. The contestant decides whether to keep their original choice, or to switch to the other closed door.
    
    The contestant wins if the door they selected in step 4 is the same as the one Monty put a prize behind in step 1.

    A contestant's strategy is given by their choices in steps 2 and 4. Write a program to determine the success rate of a contestant's strategy by simulating the game 1000 times and calculating the fraction of the times the contestant wins. Determine the success rate for these two contestants:

    Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.

    Bob chooses door #1 in step 2, and always switches to the other closed door in step 4.
    
Started: Nov 21, 2023 @ 6:45am ET
Intervals: 1
Ended: Nov 21, 2023 @ 7:15am ET

"""

# standard packages
from random import choice

# 3rd party packages

# local packages

class Player():
    def __init__(self):
        pass

class Doors():

    def __init__(self):
        self.door_one = 0
        self.door_two = 0
        self.door_three = 0
    
    def print_doors_status(self):
        print(self.door_one,
              self.door_two,
              self.door_three)
        
    def reset_doors(self):
        self.door_one = 0
        self.door_two = 0
        self.door_three = 0
    
    def open_door(self, door):
        if door == 1:
            self.door_one = 'Open'
        
        if door == 2:
            self.door_two = 'Open'    
        
        if door == 3:
            self.door_three = 'Open'


def place_prize(doors):
    door_number = choice(['ONE', 'TWO', 'THREE'])

    if door_number == 'ONE':
        doors.door_one = 1
    elif door_number == 'TWO':
        doors.door_two = 1
    elif door_number == 'THREE':
        doors.door_three = 1
    else:
        "Print no door selected."

# TODO: 
def guess_door(doors):
    door_number = choice(['ONE', 'TWO', 'THREE'])

    return door_number

# TODO: select door NOT having prize and open it
def open_door(doors):
    pass

# TODO: check if contestant guess matches where prize is
def reveal_prize(doors, guess):
    pass 

if __name__ == "__main__":

    doors = Doors()

    for i in range(1, 10):
        #reset doors for fresh run
        doors.reset_doors()
        
        #place prize
        place_prize(doors)
        
        #contestant guess
        guess = guess_door(doors)
        

        #monty open door NOT having prize and NOT guessed by contestant


        #contestant can guess again
