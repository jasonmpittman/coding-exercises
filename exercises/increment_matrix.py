__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Increment Matrix:
Write a function that takes in three parameters: r, c, i, where:

    r and c are the number of rows and columns to initialize a zero matrix.
    i represents the list of incrementing operations (+1).

And returns the resulting matrix after applying all the increment operations. Each increment operation will add 1 to the rows or columns specified in the incrementing list.

Examples:
    final(2, 2, ["0r", "0r", "0r", "1c"]) ➞ [
    [3, 4],
    [0, 1]
    ]

    final(2, 2, ["0c"]) ➞ [
    [1, 0],
    [1, 0]
    ]

    final(3, 3, ["1c", "2c", "2c", "3c", "3c", "3c"]) ➞ [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]

    final(3, 3, []) ➞ [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]

Started: Jan 28, 2024 @ 1:45pm ET
Intervals: 1
Ended: Jan 28, 2024 @ 2:15pm ET
"""
from sys import argv

# TODO: works for 2x2 but 3x3 gets a index out of range on line 70 for 'index'
def increment_matrix(number_of_rows: int, number_of_columns: int, increments: list) -> list:
    matrix = []

    # build the base matrix...is this optimal?
    for r in range(number_of_rows):
        row = []
        for c in range(number_of_columns):
            row.append(0)
        matrix.append(row)

    # loop over increments
    for increment in increments:
        # if increment is r then add 1 to index
        if 'r' in increment:
            index = int(increment[0])

            for i in range(len(matrix)):
                matrix[index][i] += 1

        # if increment is c then add 1 to index
        if 'c' in increment:
            index = int(increment[0])
        
            for i in range(len(matrix)):
                matrix[i][index] += 1
            
    print(matrix)

if __name__ == '__main__':
    number_of_rows = argv[1]
    number_of_columns = argv[2]
    increments = argv[3].split(',') # 3 3 "1c,2c,2c,3c,3c,3c"

    increment_matrix(int(number_of_rows), int(number_of_columns), increments)