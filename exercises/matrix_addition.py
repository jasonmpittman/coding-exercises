__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Matrix Addition: 
Write a function that accepts two square matrices (N x N two dimensional arrays), and return the sum of the two. Both matrices being passed into the function will be of size N x N (square), containing only integers.

Examples:
    matrixAddition(
    [ [1, 2, 3],
        [3, 2, 1],
        [1, 1, 1] ],
    //      +
    [ [2, 2, 1],
        [3, 2, 3],
        [1, 1, 3] ] )

    // returns:
    [ [3, 4, 4],
        [6, 4, 4],
        [2, 2, 4] ]

Started: May 10, 2024 @ 4:00am ET
Intervals: 1
Ended: May 10, 2024 @ 4:05am        
"""

def add_matrices(a: list, b: list) -> list:
    c = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j]) 
        
        c.append(row)

    return c

if __name__ == "__main__":
    a = [ [1, 2, 3],
        [3, 2, 1],
        [1, 1, 1] ]
    
    b = [ [2, 2, 1],
        [3, 2, 3],
        [1, 1, 3] ]

    c = add_matrices(a, b)
    print(c)
    