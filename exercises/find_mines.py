__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Find the Mines:
Write a function that accepts a 2D array, and returns the location of the mine. The mine is represented as the integer 1 in the 2D array. Areas in the 2D array that are not the mine will be represented as 0s.

The location returned should be an array (Tuple<int, int> in C#, RAX:RDX in NASM) where the first element is the row index, and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your function will be a square (NxN), and there will only be one mine in the array.

    Examples (Input --> Output)

    [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] --> [0, 0]

    [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] --> [1, 1]

    [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] --> [2, 1]

Started: Feb 12, 2025 @ 7:05am ET
Intervals: 1
Ended: Feb 12, 2025 @ 7:35am ET
"""

def find_mine(field: list) -> tuple:
    row = 0
    column = 0
    number_of_rows = len(field)
    coordinates = []
    
    for field[row] in field:
        if row <= number_of_rows:
            
            for column in field[row]:
                if field[row][column] == 1:
                    return (row, column)
                column += 1

            row += 1
        else:
            break

if __name__ == "__main__":
    field = [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ]
    coordinates = find_mine(field)
    print(coordinates)
