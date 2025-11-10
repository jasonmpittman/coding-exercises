__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
For a given list of integers, return the index of the element where the sums of the integers to the left and right of the current element are equal.

Ex:

ints = [4, 1, 7, 9, 3, 9]
# Since 4 + 1 + 7 = 12 and 3 + 9 = 12, the returned index would be 3

ints = [1, 0, -1]
# Returns None/nil/undefined/etc (depending on the language) as there
# are no indices where the left and right sums are equal

Start: 6:20am
End: 06:32am
Cycles: 1
"""

def find_midpoint_sum(array: list) -> int:
    index = 1
    limit = len(array) - 1

    while index < limit:    
        if sum(array[:index]) == sum(array[index + 1:]): 
            return index

        index += 1

if __name__ == "__main__":
    array = [1, 0, -1] # [4, 1, 7, 9, 3, 9]

    result = find_midpoint_sum(array)
    print(result)

