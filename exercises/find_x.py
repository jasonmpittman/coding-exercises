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
Ended: Mar 6th, 2025 @ 4:50am ET
"""