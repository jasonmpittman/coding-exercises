__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Maximize Number:
Write a function that makes the first number as large as possible by swapping out its digits for digits in the second number.

Examples:

    maxPossible(9328, 456) ➞ 9658
    // 9658 is the largest possible number built from swaps from 456.
    // 3 replaced with 6 and 2 replaced with 5.

    maxPossible(523, 76) ➞ 763
    maxPossible(9132, 5564) ➞ 9655
    maxPossible(8732, 91255) ➞ 9755

Started: Mar 25, 2024 @ 4:40am ET
Intervals: 1
Ended: March 25, 2024 @ 4:56am ET
"""
from sys import argv

def maximize_number(first_number: list, second_number: list) -> int:
    i = 0
    m = 0
    j = 0

    for n in first_number:
        if len(second_number) == 0:
            break

        m = max(second_number)
        
        if n < m:
            first_number[i] = m
            
            #clean up second number array
            j = second_number.index(m)
            second_number.pop(j)
    
        i += 1
    return int(''.join(first_number))


if __name__ == "__main__":
    n = argv[1]
    first_number = [x for x in n]
    
    m = argv[2]
    second_number = [x for x in m]

    print("maximizing {} from {}".format(first_number, second_number))

    result = maximize_number(first_number, second_number)
    print(result)