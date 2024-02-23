__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Matrix Zeroes:

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Examples:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Started: Feb 23, 2024 @ 3:30pm ET
Intervals: 1
Ended: Feb 23, 2024 @ 4:00pm ET
"""

# TODO: original instinct closer to correct than suggested solution
def zero_the_matrix(matrix: list) -> None:
    # if any m or n is 0, 0 both m and n

    """
    number_of_rows = len(matrix[0])
    number_of_columns = len(matrix)
    
    zeroed_matrix = []

    for i in range(number_of_columns - 1):
        for j in range(number_of_rows):
            if matrix[i][j] == 0:
                zeroed_matrix.append((i, j))

    for row, col in zeroed_matrix:
        matrix[row] = [0] * number_of_rows

        for i in range(number_of_rows):
            matrix[i][col] = 0

    print(zeroed_matrix)
    
    
    """


    n = len(matrix)
    m = len(matrix[0])

    V = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                V.append((i, j))

        for row, col in V:
            matrix[row] = [0] * m

            for i in range(n):
                matrix[i][col] = 0    


    print(V)

if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    zero_the_matrix(matrix) # outputs [(0, 0), (0, 3), (1, 0), (1, 3), (2, 0), (2, 3)]