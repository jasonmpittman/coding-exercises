__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Intersecting Ones:
Write a function that returns true if a 2D matrix is a no-intersecting ones matrix and false otherwise. A no-intersecting ones matrix is one where no two ones exist on the same row or column.

Examples:
    noIntersectingOnes([
    [0, 1],
    [1, 0]
    ]) ➞ true

    noIntersectingOnes([
    [1, 1],
    [0, 0]
    ]) ➞ false

    noIntersectingOnes([
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
    ]) ➞ true

Started: April 16, 2024 @ 5:25am ET
Intervals: 1
Ended: April 16, 2024 @ 5:55am ET
"""

def column(matrix: list, i: int) -> list:
    return [row[i] for row in matrix]

def row(matrix: list) -> list:
    return [row for row in matrix]

def is_column_intersecting(columns: list) -> bool:
    for i in range(len(columns)):
        if columns[i] == 1 and columns[i + 1] == 1:
            return True
    
    return False

def is_row_intersecting(row: list) -> bool:
    for i in range(len(matrix)):
        if matrix[i].count(1) > 1:
            return True
    
    return False


def is_matrix_intersecting(matrix: list) -> bool:
    columns = []
    for i in range(len(matrix)):
        c = column(matrix, i)
        for _ in c:
            columns.append(_)

    rows = []
    for i in range(len(matrix) - 1):
        r = row(matrix)
        for _ in r:
            rows.append(_)
    
    if is_column_intersecting(columns) == True or is_row_intersecting(rows) == True:
        return False
    else:
        return True
    

if __name__ == "__main__":
    matrix = [
       # [1, 1],
       # [0, 0]
        [0, 1],
        [1, 0]
    ]
    
    print(is_matrix_intersecting(matrix))