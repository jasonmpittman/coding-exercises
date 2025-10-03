__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that adds all the numbers together from 1 to n or, if two numbers are given: n to m. The input can be in any order.

Examples
    gauss([100]) ➞ 5050 # From the video
    gauss([5001, 7000]) ➞ 12001000 # Also ^^
    gauss([1975, 165]) ➞ 1937770

Start: 05:30am
End: 05:55:am
Cycles: 1
"""
from sys import argv

def add(m: int, n: int) -> int:
    #   (n(n+1)/2) - (m(m-1)/2)
    total = 0

    a = (m * (m - 1) // 2)
    b = (n * (n + 1) // 2)
    total = b - a

    return total

if __name__ == "__main__":
    m = int(argv[1])
    n = int(argv[2])

    result = add(m, n)
    print(result)

    