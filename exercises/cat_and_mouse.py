__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Cat and Mouse:

You will be given a string featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'. The string will start with the cat, and end with the mouse.

You need to find out if the cat can catch the mouse from its current position. The cat can jump over at most three characters. So:

"C.....m" returns "Escaped!" <-- more than three characters between

"C...m" returns "Caught!" <-- as there are three characters between the two, the cat can jump.


Started: Mar 9th, 2025 @ 6:55am ET (estimated)
Intervals: 1
Ended: Mar 9th, 2025 @ 6:59am ET
"""
import sys

def is_caught(position: str) -> bool:
    escaped = True 

    if position.count('.') > 3:
        escaped = False
    
    return escaped 

if __name__ == "__main__":
    position = sys.argv[1]

    result = is_caught(position)
    if result == True:
        print("Caught!")
    else:
        print("Escaped!")