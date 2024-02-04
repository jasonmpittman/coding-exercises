__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


""" Character Swap:

Write a function to replace all instances of character c1 with character c2 and vice versa.

Examples:
    doubleSwap( "aabbccc", "a", "b") ➞ "bbaaccc"

    doubleSwap("random w#rds writt&n h&r&", "#", "&")
    ➞ "random w&rds writt#n h#r#"

    doubleSwap("128 895 556 788 999", "8", "9")
    ➞ "129 985 556 799 888"

Started: Feb 04, 2024 @ 4:30am ET
Intervals: 1
Ended: Feb 04, 2024 @ 4:40am ET
"""
from sys import argv

def swap_character(string: str, c1: str, c2: str) -> str:
    i = 0
    my_string = list(string)
   
    for c in my_string:
        if c == c1:
            my_string[i] = c2
        
        if c == c2:
            my_string[i] = c1

        i += 1
    
    my_string = ''.join(my_string)

    print(my_string)


if __name__ == '__main__':
    string = argv[1]
    c1 = argv[2]
    c2 = argv[3]

    swap_character(string, c1, c2) # "aabbccc" "a" "b"
