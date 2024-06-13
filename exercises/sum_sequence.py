__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Sum Sequence:
Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms. This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".

Examples
    5  -->  [0,  1,  3,  6,  10,  15]
    -5  -->  [0, -1, -3, -6, -10, -15]
    7  -->  [0,  1,  3,  6,  10,  15,  21,  28]

Started: June 13, 2024 @ 5:15am ET
Intervals: 1
Ended: June 13, 2024 @ 5:21am ET
"""
from sys import argv

def sum_sequence(n: int) -> list:
    sequence = []

    for i in range(1, abs(n) + 2):
        m = sum([x for x in range(1, i)])
        
        if n < 0:
            sequence.append(m * -1)
        else:
            sequence.append(m)

    return sequence

if __name__ == "__main__":
    n = int(argv[1])

    sequence = sum_sequence(n)
    print(sequence)
