__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" New Number:
A number is input in computer then a new no should get printed by adding one to each of its digit. If you encounter a 9, insert a 10 (don't carry over, just shift things around).

For example, 998 becomes 10109.

Started: Feb 24, 2024 @ 8:50pm ET
Intervals: 1
Ended: Feb 24, 2024 @ 9:20pm ET
"""
from sys import argv

def create_new_number(number: str) -> str:
    new_number = ''

    for n in number:
        new_number += str(int(n) + 1)
    
    print(new_number)

if __name__ == "__main__":
    number = argv[1]

    create_new_number(number)