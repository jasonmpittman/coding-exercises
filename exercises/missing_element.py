__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Missing Element:
Given two integer arrays where the second array is a shuffled duplicate of the first array with one element missing, find the missing element.

Please note, there may be duplicates in the arrays, so checking if a numerical value exists in one and not the other is not a valid solution.

Examples:
    find_missing([1, 2, 2, 3], [1, 2, 3]) => 2
    find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]) => 8


Started: May 19, 2024 @ 4:40am ET
Intervals: 1
Ended: May 19, 2024 @ 4:54am
"""
from sys import argv

def find_missing_element(A: list, B: list) -> int:

    # mutate the larger list so what is left is the missing element
    for i in range(len(B)):
        if B[i] in A:
            A.remove(B[i])

    return A

if __name__ == "__main__":
    A = list(map(int, argv[1].split(','))) # 1,2,2,3 1,2,3 # 6,1,3,6,8,2 3,6,6,1,2
    B = list(map(int, argv[2].split(',')))

    missing_element = find_missing_element(A, B)
    print(missing_element)