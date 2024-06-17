__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Number Triangle:
Consider the number triangle below, in which each number is equal to the number above plus the number to the left. If there is no number above, assume it's a 0.

1
1 1
1 2 2
1 3 5 5
1 4 9 14 14
solve(5) = 42

The triangle has 5 rows and the sum of the last row is sum([1,4,9,14,14]) = 42.

You will be given an integer n and your task will be to return the sum of the last row of a triangle of n rows.

Started: June 17, 2024 @ 4:40am ET
Intervals: 1
Ended: June 17, 2024 @ 5:20am ET
"""
from sys import argv



if __name__ == "__main__":
    n = int(argv[1])