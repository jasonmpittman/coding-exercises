__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Ordered Matrix:
Create an ordered 2D array (matrix). A matrix is ordered if its (0, 0) element is 1, its (0, 1) element is 2, and so on. Your function needs to create an a × b matrix. a is the first argument and b is the second.

Examples:
    orderedMatrix(5, 5) ➞ [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
    ]

    orderedMatrix(1, 1) ➞ [[1]]
    orderedMatrix(1, 5) ➞ [[1, 2, 3, 4, 5]]

Started: Feb 01, 2024 @ 6:25am ET
Intervals: 1
Ended: Feb 01, 2024 @ 6:45am ET    
"""
from sys import argv

def create_matrix(n: int, m: int) -> list:
    product = [x for x in range(1, (n * m) + 1)]

    matrix = []
    start = 0
    stop = m

    for i in range(n):
        row = product[start:stop]
        matrix.append(row)
        start = stop + 1
        stop = stop + n

    
    return matrix

if __name__ == '__main__':
    n = int(argv[1])
    m = int(argv[2])

    matrix = create_matrix(n, m)
    print(matrix)