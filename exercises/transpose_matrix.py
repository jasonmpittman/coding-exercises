__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Transpose Matrix:
Create a function that transposes a 2D matrix.

Example:
    transposeMatrix([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
    ]) ➞ [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
    ]

    transposeMatrix([
    [5, 5],
    [6, 7],
    [9, 1]
    ]) ➞ [
    [5, 6, 9],
    [5, 7, 1]
    ]

Started: Feb 05, 2024 @ 5:35am ET
Intervals: 1
Ended: Feb 05, 2024 @ 5:54am ET
"""

def transpose_matrix(matrix: list) -> list:
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    transposed_matrix = []

    for i in range(number_of_columns):
        new_row = []
        for j in range(number_of_rows):
            new_row.append(matrix[j][i])
        
        transposed_matrix.append(new_row)
    
    return transposed_matrix

if __name__ == '__main__':
    matrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
    ]

    '''matrix = [
    [5, 5],
    [6, 7],
    [9, 1]
    ]'''

    transposed_matrix = transpose_matrix(matrix)
    print(transposed_matrix)