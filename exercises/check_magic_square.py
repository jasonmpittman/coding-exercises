__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Check Magic Square: https://edabit.com/challenge/iYcNv2tDvNgnSsG9S
A "magic square" is a square divided into smaller squares each containing a number, such that the numbers in each vertical, horizontal, and diagonal row add up to the same value.

Write a function that takes a 2D array, checks if it's a magic square and returns either true or false depending on the result.

Examples:
    isMagicSquare([
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
    ]) ➞ true

    isMagicSquare([
    [16,  3,  2, 13],
    [ 5, 10, 11,  8],
    [ 9,  6,  7, 12],
    [ 4, 15, 14,  1]
    ]) ➞ true

    isMagicSquare([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]) ➞ false


Started: Mar 09, 2024 @ 5:40pm ET
Intervals: 1
Ended: March 09, 2024 @ 6:05pm ET
"""

def is_magic_square(square: list) -> bool:
    sums = []
    # returns sum of each row
    for i in range(len(square)): #rows
        sums.append(sum(square[i]))

    # returns sum of each column
    for i in range(len(square)):
        sums.append(sum([column[i] for column in square]))

    # returns sum of each diagonal
    front_diagonal = [square[i][i] for i in range(len(square))]
    sums.append(sum(front_diagonal))    

    back_diagonal = [row[-i-1] for i, row in enumerate(square)]
    sums.append(sum(back_diagonal))

    return all(i == sums[0] for i in sums) # new use of all()

if __name__ == "__main__":
    # is not magic square
    square = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    # is magic square
    #square =[[8, 1, 6],
    #[3, 5, 7],
    #[4, 9, 2]]

    result = is_magic_square(square)
    print(result)