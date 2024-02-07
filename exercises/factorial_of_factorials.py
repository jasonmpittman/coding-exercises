__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Factorial of Factorials:
Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

Examples:
    fact_of_fact(4) ➞ 288
    # 4! * 3! * 2! * 1! = 288

    fact_of_fact(5) ➞ 34560
    fact_of_fact(6) ➞ 24883200

Started: Feb 07, 2024 @ 4:50am ET
Intervals: 1
Ended: Feb 07, 2024 @ 5:07am ET
"""
from sys import argv

def factorial_of_factorials(n: int) -> int:
    factorial = 1

    for x in range(1, n + 1):
        for i in range(1, x + 1):
            factorial = factorial * i
    
    print(factorial)


if __name__ == '__main__':
    n = int(argv[1])
    factorial_of_factorials(n)