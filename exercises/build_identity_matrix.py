__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

Examples
    id_mtrx(2) ➞ [
    [1, 0],
    [0, 1]
    ]
    id_mtrx(-2) ➞ [
    [0, 1],
    [1, 0]
    ]
    id_mtrx(0) ➞ []

Start: 05:20am
End: 05:50:am
Cycles: 1
"""
from sys import argv

def build_identity_matrix(n: int) -> list:
    matrix = []

    #   handles positive integer n    
    if n >= 0:
        for i in range(n):
            row = []
            col_count = 0
            for j in range(n):
                if col_count == i:
                    row.append(1)
                    col_count += 1
                else:
                    row.append(0)
                    col_count += 1
            
            matrix.append(row)

    #   TODO: not handling correctly
    #   handles negative integer n
    if n < 0:
       for i in range(abs(n)):
            row = []
            col_count = 0
            for j in range(abs(n)):
                if col_count == i:
                    row.append(0)
                    col_count += 1
                elif col_count == i + 1:
                    row.append(0)
                    col_count += 1
                else:
                    row.append(1)
                    col_count += 1
            
            matrix.append(row)

    return matrix        

if __name__ == "__main__":
    n = int(argv[1])

    identity_matrix = build_identity_matrix(n)
    print(identity_matrix)



