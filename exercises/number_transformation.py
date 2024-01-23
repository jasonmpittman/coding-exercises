__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Number Transformation:

You are given two positive integers n and m. You have to perform some basic mathematical operations on n to obtain m. These are your options:

(n-1)/2   - if (n-1) is divisible by 2
n/2       - if n is divisible by 2
n*2

Create a function that returns the minimum number of steps required to transform n into m.

Examples:
    number_transform(2, 8) ➞ 2
    // 2 * 2 = 4
    // 4 * 2 = 8

    number_transform(9, 2) ➞ 2
    // (9-1) / 2 = 4
    // 4 / 2 = 2

    number_transform(1024, 1024) ➞ 0

Started: Jan 23, 2024 @ 5:45am ET
Intervals: 1
Ended: Jan 23, 2024 @ 6:15am ET
"""
from sys import argv

# TODO: 2,8 or similar causes an inifinite loop. the problems is flawed. 9,2 works as expected.
def transform_number(n: int, m: int):
    steps = 0

    while n != m:
        if n < m:
            print("Entering case 0")
            n = n * 2
            steps += 1
        if (n - 1) % 2 == 0:
            print("Entering case 1")
            n = (n - 1) / 2
            steps += 1
        elif n % 2 == 0:
            print("Entering case 2")
            n = n / 2
            steps += 1
        else:
            print("Entering case 3")
            n = n * 2
            steps += 1

    print(steps)

if __name__ == '__main__':
    n, m = argv[1].split(',')
    transform_number(int(n), int(m))
