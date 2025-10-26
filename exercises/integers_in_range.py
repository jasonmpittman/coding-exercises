__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that validates whether numbers x and y are within the bounds of lower and upper. Return false if n is not an integer.

Examples
    intWithinBounds(3, 1, 9) ➞ true
    intWithinBounds(6, 1, 6) ➞ false
    intWithinBounds(4.5, 3, 8) ➞ false

Start: 02:05pm
End: 02:35pm
Cycles: 1
"""
from sys import argv

def is_within_bounds(x: int, y: int, lower: int, upper: int) -> bool:

    if x in range(lower, upper) and y in range(lower, upper):
        return True
    else:
        return False

if __name__ == "__main__":
    x, y, lower, upper = int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4])
    
    result = is_within_bounds(x, y, lower, upper)
    print(result)