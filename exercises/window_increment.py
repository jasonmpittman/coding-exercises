__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Window Increment: 
Create a function that takes three integer parameters: a number n, number of iterations, and step. You have to implement an algorithm, which increases the given number as explained below:

s - Starting Position
* - current increased position

Position: s - - - - - ➞ - - - * - -
Number:   1 4 3 7 2 6 ➞ 1 4 3 8 2 6

s - Starting Position
* - current increased position

Position: - - - s - - ➞ * - - - - -
Number:   1 4 3 8 2 6 ➞ 2 4 3 8 2 6

Remember, if the number overflows, the current position gets shifted to the right.

9 9 9 ➞ - - p   // before overflow position will be at 3rd digit
1 0 0 0 ➞ - - - p   // after overflow position will be at 4th digi

Examples:
    simpleIncrement(1673, 2, 16) ➞ 3673
    simpleIncrement(99, 99, 99) ➞ 198
    simpleIncrement(99, 99, 98) ➞ 4734

Started: Jan 31, 2024 @ 7:50am ET
Intervals: 1
Ended: Jan 31, 2024 @ 8:20am ET
"""
from sys import argv

# TODO: close - need to replace '1' with '3'
def window_increment(n: int, iterations: int, step: int) -> int:
    final_number = str(n)
    i = 0
    j = step

    for iteration in range(iterations):
        value = final_number[i % len(final_number)]
        index = final_number.index(value)
        
        # add 1 to the integer at index in final_number
        final_number = str(int(final_number[index]) + 1) + final_number[index:]
        
        
        i = i + j

    return final_number

if __name__ == '__main__':
    # 1673 2 16
    n = int(argv[1])
    iterations = int(argv[2])
    step = int(argv[3])

    print(window_increment(n, iterations, step))