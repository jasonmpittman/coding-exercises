__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Sort Odds:
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
    [7, 1]  =>  [1, 7]
    [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

Started: June 03, 2024 @ 6:00am ET
Intervals: 1
Ended: June 03, 2024 @ 6:10am ET
"""
from sys import argv

def sort_odds(array: list) -> list:
    # extract odd integers from array
    odds = [(index, number) for index, number in enumerate(array) if number % 2 != 0]
    
    # sort the odds integers
    sorted_odds = sorted([num for _, num in odds])

    # reinsert the odds in array
    for (index, _), num in zip(odds, sorted_odds):
        array[index] = num

    print(array)

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    sort_odds(array)