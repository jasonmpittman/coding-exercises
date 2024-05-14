__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Largest Product Series:
Write a function that will find the greatest product of five consecutive digits in the given string of digits.

Example: 
    "123834539327238239583" is 3240.

Started: May 14, 2024 @ 3:45am ET
Intervals: 1
Ended: May 14, 2024 @ 3:55am
"""
from sys import argv
import functools
import operator

def find_greatest_product(series: str) -> int:
    head = 0
    tail = 5
    greatest = 0

    while tail <= len(series):
        subseries = series[head:tail]
        product = functools.reduce(operator.mul, [int(x) for x in subseries])
    
        if product > greatest:
            greatest = product
        
        head += 1
        tail += 1

        #print("Current greatest is: ", greatest)

    return greatest

if __name__ == "__main__":
    series = argv[1] # 123834539327238239583 # 92494737828244222221111111532909999 -> 5292

    product = find_greatest_product(series)
    print(product)
