__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""" Next Largest Integer:
Given an integer, find the next largest integer using ONLY the digits from the given integer.

Examples:
    Input:
        1234
        1243
        234765
        19000
    Output:
        1243
        1324
        235467
        90001


Started: Feb 22, 2024 @ 5:00am ET
Intervals: 1
Ended: Feb 22, 2024 @ 5:30am ET
"""
from sys import argv
from itertools import permutations

# TODO: bug where 19000 returns 19000...all other test cases pass
def find_next_largest(numbers: list, number: int):
    largest_integer = 0

    i = numbers.index(number)
    largest_integer = numbers[i + 1]

    print(largest_integer)

if __name__ == "__main__":
    number = argv[1]
    
    permutations_of_number = permutations(number)
    possible_numbers = [''.join(x) for x in permutations_of_number]
    print(sorted(possible_numbers))

    find_next_largest(sorted(possible_numbers), number)
    