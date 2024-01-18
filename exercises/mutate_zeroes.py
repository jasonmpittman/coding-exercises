__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Mutate Zeroes:
Write a function that moves all the zeroes to the end of a list. Do this without returning a copy of the input list.
    You must mutate the original list.
    Keep the relative order of the non-zero elements the same.

Examples:
    zeroes_to_end([1, 2, 0, 0, 4, 0, 5]) ➞ [1, 2, 4, 5, 0, 0, 0]
    zeroes_to_end([0, 0, 2, 0, 5]) ➞ [2, 5, 0, 0, 0]
    zeroes_to_end([4, 4, 5]) ➞ [4, 4, 5]
    zeroes_to_end([0, 0]) ➞ [0, 0]

Started: Jan 18, 2024 @ 7:00am ET
Intervals: 1
Ended: Jan 18, 2024 @ 7:13am ET
"""
from sys import argv

def mutate_list(l : list) -> list:
    
    for c in l:
        if c == "0":
            l.remove(c)
            l.insert(len(l), c)
        
    print("After mutation: ", l)
    

if __name__ == '__main__':
    # test lists: 1,2,0,0,4,0,5 ; 0,0,2,0,5
    l = argv[1].split(',') 
    print("Before mutation: ", l)
    
    mutate_list(l)