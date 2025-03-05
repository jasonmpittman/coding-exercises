__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Find X:
We have a function that takes in an integer n, and returns a number x.

Lets call this function findX(n)/find_x(n) (depending on your language):

def find_x(n):
    x = 0
    for i in range(n):
        for j in range(2*n):
            x += j + i
    return x

The functions loops throught the number n and at every iteration, performs a nested loop on 2*n, at each iteration of this nested loop it increments x with the (nested loop index + parents loop index).

This works well when the numbers are reasonably small.

find_x(2) #=> 16
find_x(3) #=> 63
find_x(5) #=> 325

But may be slow for numbers > 103

So your task is to optimize the function findX/find_x, so it works well for large numbers.


Started: Mar 6th, 2025 @ 4:20am ET (estimated)
Intervals: 1
Ended: Mar 6th, 2025 @ 4:39am ET
"""
import sys
from time import process_time_ns

def find_x(n: int) -> int:
    x = 0
    for i in range(n):
        for j in range(2*n):
            x += j + i
    return x

def find_x_optimized(n: int) -> int:
    x = 0

    for i in range(n):
        x += sum([j + i for j in range(2*n)])

    return x

if __name__ == "__main__":
    n = int(sys.argv[1])

    t = process_time_ns()
    result = find_x(n)
    elapsed_time = process_time_ns() - t

    print("Obtained {} in {} nanoseconds".format(result, elapsed_time))

    t_optimized = process_time_ns()
    optimized_result = find_x_optimized(n)
    elapsed_optimized_time = process_time_ns() - t_optimized

    print("Obtained {} in {} nanoseconds".format(result, elapsed_optimized_time))