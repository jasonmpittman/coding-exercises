__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Sum Multiples:

Return the sum of the multiples of 3 and 5 below a number

Started: Mar 10th, 2025 @ 6:20am ET
Intervals: 1
Ended: Mar 7th, 2025 @ 6:28am ET
"""

import sys

def get_multiples(n: int) -> list:
    multiples = []

    for x in range(1, n):
        if x % 3 == 0:
            multiples.append(x)
        
        if x % 5 == 0:
            multiples.append(x)

    return multiples

def sum_multiples(multiples: list) -> int:
    return sum(set(multiples))



if __name__ == "__main__":
    n = int(sys.argv[1])

    multiples = get_multiples(n)
    summed = sum_multiples(multiples)

    print(summed)