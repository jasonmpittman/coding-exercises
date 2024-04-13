__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


""" Grey Code:
A Gray code is a list of all 2^n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one). The task is to create a Gray code for a given length n.

Input
The only input line has an integer n.

Output
Print 2^n lines that describe the Gray code. You can print any valid solution.


Example
    Input:
    2

    Output:
    00
    01
    11
    10

Started: April 13, 2024 @ 5:00am ET
Intervals: 1
Ended: April 13, 2024 @ 5:30am ET
"""
from sys import argv


def calculate_hamming_distance(string_a: str, string_b: str) -> int:
    """ Calculate the edit distance between two strings """
    edits = 0

    if len(string_a) != len(string_b):
        print("Strings are not of equal length")
    else:
        for x,(i, j) in enumerate(zip(string_a, string_b)):
            if i != j:
                edits += 1
    
    return edits

def build_bit_strings(n):
    strings = []

    def genbin(n, bs=''):
        if len(bs) == n:
            strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')


    genbin(n)
    return strings

#TODO: this works for n = 1, 2 but need to test for n > 2
def generate_grey_code(n: int) -> list:
    strings = build_bit_strings(n) # for n = 2, returns ['00', '01', '10', '11']
    
    for i in range(len(strings) - 1):
        if calculate_hamming_distance(strings[i], strings[i+1]) > 1:
            strings.insert(len(strings), strings.pop(i+1))

    return strings

if __name__ == "__main__":
    n = int(argv[1])

    grey_code = generate_grey_code(n)
    print(grey_code)
