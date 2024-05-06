__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Farm Problem:
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

    chickens = 2 legs
    cows = 4 legs
    pigs = 4 legs

The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.

Examples
    animals(2, 3, 5) ➞ 36
    animals(1, 2, 3) ➞ 22
    animals(5, 2, 8) ➞ 50

Started: May 06, 2024 @ 6:05am ET
Intervals: 1
Ended: May 06, 2024 @ 6:07am ET
"""
from sys import argv

def count_animal_legs(chickens: int, cows: int, pigs: int) -> int:
    total_legs = (chickens*2) + (cows*4) + (pigs*4)

    return total_legs


if __name__ == "__main__":
    chickens = int(argv[1])
    cows = int(argv[2])
    pigs = int(argv[3])

    result = count_animal_legs(chickens, cows, pigs)
    print(result)