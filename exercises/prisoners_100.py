__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" 100 Prisoners: https://rosettacode.org/wiki/100_prisoners
The Problem

    100 prisoners are individually numbered 1 to 100
    A room having a cupboard of 100 opaque drawers numbered 1 to 100, that cannot be seen from outside.
    Cards numbered 1 to 100 are placed randomly, one to a drawer, and the drawers all closed; at the start.
    Prisoners start outside the room

        They can decide some strategy before any enter the room.
        Prisoners enter the room one by one, can open a drawer, inspect the card number in the drawer, then close the drawer.
        A prisoner can open no more than 50 drawers.
        A prisoner tries to find his own number.
        A prisoner finding his own number is then held apart from the others.

    If all 100 prisoners find their own numbers then they will all be pardoned. If any don't then all sentences stand.


The task

    Simulate several thousand instances of the game where the prisoners randomly open drawers
    Simulate several thousand instances of the game where the prisoners use the optimal strategy mentioned in the Wikipedia article, of:

        First opening the drawer whose outside number is his prisoner number.
        If the card within has his number then he succeeds otherwise he opens the drawer with the same number as that of the revealed card. (until he opens his maximum).

Output:
    Simulation count: 100000
    Random play wins:  0.0% of simulations
    Optimal play wins: 31.1% of simulations

Started: Jan 21, 2024 @ 5:35am ET
Intervals: 1
Ended: Jan 21, 2024 @ 6:05am ET
"""
import random

def create_cupboard(size: int) -> dict:
    cupboard = {}

    for i in range(1, size + 1):
        cupboard[i] = random.randint(1, size)

    return cupboard

def search_blind_cupboard(cupboard: dict, number_of_prisoners=100, number_of_tries=50) -> int:
    number_of_wins = 0
    number_of_searches = 0

    for prisoner in range(1, number_of_prisoners):
        prisoner_attempts = number_of_tries
        
        while prisoner_attempts > 0:
            drawer = random.randint(1, len(cupboard))
            #print("Prisoner {} is searching drawer {} for attempt {}".format(prisoner, cupboard[drawer], prisoner_attempts))
            
            if cupboard[drawer] == prisoner:
                number_of_wins += 1
                break

            prisoner_attempts -= 1
            number_of_searches += 1

    return number_of_wins, number_of_searches

# TODO: implement optimal strategy
def search_strategy_cupboard():
    pass

# TODO: implement exact output by converting to %
if __name__ == '__main__':
    cupboard_size = 100
    number_of_prisoners = 100
    search_attempts = 50

    cupboard = create_cupboard(cupboard_size)
    number_of_wins, number_of_searches = search_blind_cupboard(cupboard, number_of_prisoners, search_attempts)
    
    print("Simulation count: ", number_of_searches)
    print("Number of wins: ", number_of_wins)
    