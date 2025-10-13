__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function that takes in three parameters: r, c, i, where:

    r and c are the number of rows and columns to initialize a zero matrix.
    i represents the list of incrementing operations (+1).

And returns the resulting matrix after applying all the increment operations. Each increment operation will add 1 to the rows or columns specified in the incrementing list.

final(3, 3, ["2r", "2c", "1r", "0c"])

# Initialize a 3 x 3 matrix of zeroes.

[
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

# Apply "2r" (increment index 2 row).

[
  [0, 0, 0],
  [0, 0, 0],
  [1, 1, 1]
]

# Apply "2c" (increment index 2 column).

[
  [0, 0, 1],
  [0, 0, 1],
  [1, 1, 2]
]

# Apply "1r" (increment index 1 row).

[
  [0, 0, 1],
  [1, 1, 2],
  [1, 1, 2]
]

# Apply "0c" (increment index 0 column).
# This is the result you should return.

[
  [1, 0, 1],
  [2, 1, 2],
  [2, 1, 2]
]

Start: 06:00am
End: 06:30:am
Cycles: 1
"""

def initialize_matrix(r: int, c: int) -> list:
    """ List comprehension initialization of 0s matrix """
    matrix = [[0 for _ in range(n)] for _ in range(m)]

    return matrix


def increment_rows_columns(r: int, c: int, increments: list) -> list:
    matrix = initialize_matrix(r, c)

    for increment in increments:
        print(f'working on {increment}')

        location = int(increment[0])
        r_or_c = increment[1]
        
        #   location is row r
        if r_or_c == 'r':
            row = matrix[location]
            for i in range(len(row)):
                matrix[location][i] += 1            

        #   location is column c
        elif r_or_c == 'c':
            pass

    return matrix

if __name__ == "__main__":
    m = 3
    n = 3
    increments = ["2r", "2c", "1r", "0c"]

    matrix = increment_rows_columns(m, n, increments)
    
    for i in range(len(matrix)):
        print(matrix[i])