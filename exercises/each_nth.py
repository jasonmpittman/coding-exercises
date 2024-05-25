
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Each Nth:

In this task, you need to write a function each, that takes an integer number n and a ( possibly empty ) list of integers, and returns a list of every nth element of the input list ( which possibly is the empty list ).

If n < 0, count by abs n from the end of the list.
If n == 0, return an empty list.

Examples
    each 0 [1,2,3,4,5,6] = []  
    each 1 [1,2,3,4,5,6] = [1,2,3,4,5,6]  
    each (-1) [1,2,3,4,5,6] = [6,5,4,3,2,1]  
    each 2 [1,2,3,4,5,6] = [2,4,6]  
    each (-2) [1,2,3,4,5,6] = [5,3,1]  
    each 3 [1,2] = []  
    each (-3) [1,2] = []  
    each 5 [1,2,3,4,5,6,7] = [5]  
    each (-5) [1,2,3,4,5,6,7] = [3]  

Started: May 26, 2024 @ 6:00am ET
Intervals: 1
Ended: May 26, 2024 @ 6:30am ET
"""
from sys import argv

def each_nth(array: list, n: int) -> list:
    nth = []
    for i in range(n, len(array) + n, n):
        nth.append(i)

    return nth


if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    n = int(argv[2])

    nth = each_nth(array, n)
    print(nth)