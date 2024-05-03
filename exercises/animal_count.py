__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Animal Count:

Farmer Bob have a big farm, where he growths chickens, rabbits and cows. It is very difficult to count the number of animals for each type manually, so he diceded to buy a system to do it. But he bought a cheap system that can count only total number of heads, total number of legs and total number of horns of animals on the farm. Help Bob to figure out how many chickens, rabbits and cows does he have?

All chickens have 2 legs, 1 head and no horns; 
All rabbits have 4 legs, 1 head and no horns; 
All cows have 4 legs, 1 head and 2 horns.

Your task is to write a function, which returns a dictionary:

{"rabbits" : rabbits_count, "chickens" : chickens_count, "cows" : cows_count}

Parameters legs_number, heads_number, horns_number are integer, all tests have valid input.

Example:

get_animals_count(34, 11, 6); # Should return {"rabbits" : 3, "chickens" : 5, "cows" : 3}
get_animals_count(154, 42, 10); # Should return {"rabbits" : 30, "chickens" : 7, "cows" : 5}


Started: May 03, 2024 @ 4:10am ET
Intervals: 1
Ended: May 03, 2024 @ 4:40am ET
"""
from sys import argv
import math

# TODO: works for first example but not second? the temp_legs hack is flawed
def get_animal_counts(legs: int, heads: int, horns: int) -> dict:
    animals = {'rabbits': 0, 'chickens': 0, 'cows': 0}

    # get cows
    if horns != 0:
        number_of_cows = horns // 2
        legs = legs - (number_of_cows * 4)
        heads = heads - number_of_cows
    
    animals['cows'] = number_of_cows
    #print("Cows: ", number_of_cows)

    # get rabbits
    if legs % 2 == 0:
        temp_legs = legs // 2
        number_of_rabbits = math.ceil(temp_legs / 4)
        legs = legs - (number_of_rabbits * 4)
        heads = heads - number_of_rabbits

    #print("Rabbits: ", number_of_rabbits)
    animals['rabbits'] = number_of_rabbits

    # get chickens
    number_of_chickens = legs // 2

    #print("Chickens: ", number_of_chickens)
    animals['chickens'] = number_of_chickens

    return animals

# 34, 11, 6
if __name__ == "__main__":
    legs = int(argv[1]) 
    heads = int(argv[2])
    horns = int(argv[3])

    animals = get_animal_counts(legs, heads, horns)
    print(animals)