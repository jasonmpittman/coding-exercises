__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Burrows-Wheeler Transform:


Examples: 
    bwTransform("banana$") ➞ "annb$aa"
    bwTransform("mississippi$") ➞ "ipssm$pissii"
    bwTransform("acccgtttgtttcaatagatccatcaa$") ➞ "aacc$tacgttctaccatcaatatttgg"

Started: Mar 13, 2024 @ 5:05pm ET
Intervals: 1
Ended: March 13, 2024 @ 5:35pm ET
"""
from sys import argv




if __name__ == "__main__":
    string = argv[1]

