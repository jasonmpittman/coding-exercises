__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Rotate Matrix:
Rotate a given matrix 90 degrees to the left.

Example:
    Input: {{-1, 4, 5},
            { 2, 3, 4}}

    Output: {{ 5, 4},
            { 4, 3},
            {-1, 2}}

Started: May 30, 2024 @ 5:40am ET
Intervals: 1
Ended: May 30, 2024 @ 6:10am ET
"""

def rotate_matrix(matrix: list) -> list:
    # Transpose the matrix to convert rows to columns using zip and then reverse each row
    rotated_matrix = [list(row) for row in zip(*matrix)][::-1]

    for row in rotated_matrix:
        print(row)


if __name__ == "__main__":
    matrix = [[-1, 4, 5], [2, 3, 4]]
    rotate_matrix(matrix)