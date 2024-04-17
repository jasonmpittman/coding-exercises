__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Array to Set: 
Create a function that sorts a list and removes all duplicate items from it. Output list.

Examples:
    set([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
    set([4, 4, 4, 4]) ➞ [4]
    set([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
    set([3, 3, 3, 2, 1]) ➞ [1, 2, 3]

Started: April 17, 2024 @ 5:40am ET
Intervals: 1
Ended: April 17, 2024 @ 6:10am ET
"""
from sys import argv

#TODO: small bug check ex 2 and 4
def remove_duplicates(array: list) -> list:
    for i in array:
        for j in range(1, len(array) - 1):
            if i == array[j]:
                array.pop(j)

    return array

def convert_to_set(array: list, cast="no") -> list:
    if cast == "yes":
        print("Using cast method")
        return set(array)
    
    if cast == "no":
        print("Using manual method")
        # sort the list
        sorted_array = sorted(array)

        # loop and if i == j, remove
        return remove_duplicates(sorted_array)

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    cast = argv[2]

    result = convert_to_set(array, cast)
    print(result)