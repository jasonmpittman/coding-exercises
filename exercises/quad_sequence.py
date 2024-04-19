__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Quad Sequence:
Write a function that receives an array of x integers and returns an array of x integers in the Nth term of a quadratic number sequence (where x is the length of the incoming array). Your function should return the continuation of the quadratic sequence of the length equal to the length of the given array.

Examples
    quadSequence([48, 65, 84]) ➞ [105, 128, 153]
    quadSequence([0, 1, 6, 15, 28]) ➞ [45, 66, 91, 120, 153]
    quadSequence([9, 20, 33, 48]) ➞ [65, 84, 105, 128]

Started: April 19, 2024 @ 7:10am ET
Intervals: 1
Ended: April 19, 2024 @ 7:40am ET
"""
from sys import argv

# TODO: follow algorithm here: https://thirdspacelearning.com/gcse-maths/algebra/quadratic-sequences/
def generate_sequence(sequence: list) -> list:
    # an**2 + bn + c
    first_differences = []
    second_differences = []
    halved_difference = 0
    length = len(sequence)

    # find first difference between terms
    for i in range(length - 1):
        first_differences.append(sequence[i + 1] - sequence[i])

    # find second difference between terms
    for i in range(len(first_differences) - 1):
        second_differences.append(first_differences[i + 1] - first_differences[i])

    # half the second difference (we assume it is the same value...should check b/c not quadractic if false)
    halved_difference = second_differences[0] // 2
    
    # substract an**2 from the original sequence... so 48 - 48*1**2 = 0, 65 - 65*2**2 = 0, 84 - 84*1**2 = 0

    # is new sequence linear?



if __name__ == "__main__":
    sequence = list(map(int, argv[1].split(','))) # 48,65,84

    generate_sequence(sequence)