__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Identity Matrix:
Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

Examples:
    id_mtrx(2) ➞ [
    [1, 0],
    [0, 1]
    ]

    id_mtrx(-2) ➞ [
    [0, 1],
    [1, 0]
    ]

    id_mtrx(0) ➞ []

Started: Jan 12, 2024 @ 4:20am ET
Intervals: 1
Ended: Jan 12, 2024 @ 4:50am ET
"""
from sys import argv

#TODO: this could be refactored into list comprehensions
def generate_matrix(n: int) -> list:
    matrix = []
    
    if n >= 0:
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            
            matrix.append(row)
    else:
        for i in range(-n): #this works for a 2x2 but not >= 3x3 matrices?
            row = []
            for j in range(-n):
                if i == j: # to fix the bug we need to ensure there is only 1 per row
                    row.append(0)
                else:
                    row.append(1)
            
            matrix.append(row)            

    return matrix

if __name__ == '__main__':
    n = int(argv[1])

    print(generate_matrix(n))