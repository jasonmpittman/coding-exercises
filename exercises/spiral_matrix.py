__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Spiral Matrix:
Given an m x n matrix, return all elements of the matrix in spiral order.

Examples:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Started: April 30, 2024 @ 2:20am ET
Intervals: 1
Ended: April 30, 2024 @ 2:47am ET
"""

# assumes 3xn matrix
def find_spiral(matrix: list) -> list:
    m = len(matrix) #rows
    n = len(matrix[0]) #columns
    spiral = []

    # iterate first row
    for i in matrix[0]:
        spiral.append(i)

    # iterate last column
    last_column = [col[n - 1] for col in matrix]
    for i in last_column[1:]:
        spiral.append(i)

    # iterate last row in reverse
    for i in sorted(matrix[m - 1], reverse=True):
        if i not in spiral:
            spiral.append(i)

    # iterate first column in reverse minus first row
    first_column = [col[0] for col in matrix]
    print(first_column)
    for i in sorted(first_column, reverse=True):
        if i not in spiral:
            spiral.append(i)

    # iterature middle row minus last column
    for i in matrix[1]:
        if i not in spiral:
            spiral.append(i)
    
    return spiral

if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    #matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

    spiral = find_spiral(matrix)
    print(spiral)