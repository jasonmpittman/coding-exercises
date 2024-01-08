__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Tower of Hanoi:
Create a function that takes a number discs as an argument and returns the minimum amount of steps needed to complete the game.

Examples:
    towerHanoi(3) ➞ 7
    towerHanoi(5) ➞ 31
    towerHanoi(0) ➞ 0

Started: Jan 08, 2024 @ 5:15am ET
Intervals: 1
Ended: Jan 08, 2024 @ 5:20am ET
"""
from sys import argv

def count_number_of_steps(n: int) -> int:
    return 2**n - 1


if __name__ == '__main__':
    n = int(argv[1])
    number_of_steps = count_number_of_steps(n)

    print(number_of_steps)
