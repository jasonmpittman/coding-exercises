__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Missing Number: https://cses.fi/problemset/task/1083/

You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
ß
Input

    The first input line contains an integer n.

    The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
    Output

    Print the missing number.

Constraints
    2 <= n <= 2 * 10^5

Example
    Input:
    5
    2 3 1 5

    Output:
    4

Started: Jan 27, 2024 @ 5:20am ET
Intervals: 1
Ended: Jan 27, 2024 @ 5:32am ET
"""
from sys import argv

def find_missing_number(n: int, numbers: list) -> int:
    missing_number = 0

    expected_sum = (n * (n + 1)) // 2
    real_sum = 0

    # could use the sum() method here
    for i in numbers:
        real_sum += i

    missing_number = expected_sum - real_sum 

    return missing_number


if __name__ == '__main__':
    # 5 "2,3,1,5"
    n = int(argv[1])
    numbers = [int(x) for x in argv[2].split(',')] 

    print(find_missing_number(n, numbers))
    