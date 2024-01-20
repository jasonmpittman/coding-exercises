__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Staircase:
Write a function which takes an integer steps and returns a string representing an upward stair with steps representing the number of the steps in the stair. Each step will be represented by combinations of underscore(s), newline(s), and vertical line(s).

So, if you print the result for a stair with three steps, it will look something like this:

      _
    _|
  _|
_|

Examples:
    stair(1)  ➞ "  _\n_|"
    # 2 spaces, 1 underscore, 1 newline, 1 underscore, 1 vertical line

    stair(2)  ➞ "    _\n  _|\n_|"
    # 4 spaces, 1 undescore, 1 newline, 2 spaces, 1 underscore,
    # 1 vertical line, 1 newline, 1 underscore, 1 vertical line

    stair(3) ➞ "      _\n    _|\n  _|\n_|"
    # 6 spaces, 1 undescore, 1 newline, 4 spaces, 1 underscore,
    # 1 vertical line, 1 newline, 2 spaces, ...

    stair(4) ➞ "        _\n      _|\n    _|\n  _|\n_|"
    # 8 spaces, 1 undescore, 1 newline, 6 spaces, 1 underscore,
    # 1 vertical line,  ...

    For zero, return ___ (three underscores).

Started: Jan 20, 2024 @ 5:05am ET
Intervals: 1
Ended: Jan 20, 2024 @ 5:26am ET
"""
from sys import argv

def build_staircase(n: int):
    staircase = None

    if n == 0:
        print("___")
    
    if n == 1:
        print("  _\n_|")
    
    if n >= 2:
        i = 0
        interval = n
        staircase = (" " * n) + "  _\n" # creates bottom stair
        while i < n:
            staircase = staircase + (" " * interval) + "_|\n"
            interval -= 1
            i += 1 

        #staircase = staircase + "\n_|"
        print(staircase)

if __name__ == '__main__':
    n = int(argv[1])

    build_staircase(n)