__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Histogram: 

Build a function that creates histograms. Every bar needs to be on a new line and its length corresponds to the numbers in the array passed as an argument. The second argument of the function represents the character to be used for the bar.

histogram(arr, char) ➞ str

Example:

histogram([1, 3, 4], "#") ➞ "#\n###\n####"

    #
    ###
    ####

Started: Feb 03, 2024 @ 10:20am ET
Intervals: 1
Ended: Feb 03, 2024 @ 10:25am ET
"""
from sys import argv

def draw_histogram(bar_lengths: list, character: str):
    for bar in bar_lengths:
        print(character * int(bar))


if __name__ == '__main__':
    bar_lengths = argv[1].split(',')
    character = argv[2]
    
    draw_histogram(bar_lengths, character)