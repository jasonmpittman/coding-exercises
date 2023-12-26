__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Sudoku Checker:

Write a Python function that checks if a given 9x9 Sudoku board is valid. A Sudoku board is valid if each row, each column, and each of the nine 3x3 sub-boxes of the grid contain all of the digits from 1 to 9.

The function should return True if the Sudoku board is valid according to the mentioned rules, and False otherwise.

Started: Dec 26, 2023 @ 6:00am ET
Intervals: 1
Ended: Dec 26, 2023 @ 6:30am ET
"""

def is_valid_sudoku(board):
    
    pass

if __name__ == '__main__':
    board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]