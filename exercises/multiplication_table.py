__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Multiplication Table:
Your task, is to create N x N multiplication table, of size n provided in parameter.

For example, when n is 5, the multiplication table is:

    1, 2, 3, 4, 5
    2, 4, 6, 8, 10
    3, 6, 9, 12, 15
    4, 8, 12, 16, 20
    5, 10, 15, 20, 25

    [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

Examples:

    multiplicationTable(1) ➞ [[1]]
    multiplicationTable(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


Started: Mar 20, 2024 @ 5:35am ET
Intervals: 1
Ended: March 20, 2024 @ 6:05am ET
"""
from sys import argv

def build_multiplication_table(n: int) -> list:
    table = []
    start = 1
    stop = n + 1
    product = n * n

    for i in range(1, n + 1): # this will generate 1 - product
        table.append([x for x in range(start, stop)])
        start = stop
        stop = stop + n
            
    return table


if __name__ == "__main__":
    n = int(argv[1])

    table = build_multiplication_table(n)
    
    for t in table:
        print(t)