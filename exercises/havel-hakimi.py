#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


"""Havel-Hakimi Algorithm: https://old.reddit.com/r/dailyprogrammer/comments/bqy1cf/20190520_challenge_378_easy_the_havelhakimi/


    Remove all 0's from the sequence
    If the sequence is now empty (no elements left), stop and return true
    Sort the sequence in descending order 
    Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and call it N. The sequence is now 1 shorter than it was after the previous step
    If N is greater than the length of this new sequence, stop and return false
    Subtract 1 from each of the first N elements of the new sequence
    Continue from step 1 using the sequence from the previous step

Test strings:
5 3 0 2 6 2 0 7 2 5 => False TODO: this is returning True
3 1 2 3 1 0 => True
1 => False
[] => True

Started: Nov 23, 2023 @ 6:20am ET
Intervals: 1
Ended: Nov 23, 2023 @ 6:50am ET

"""

# standard packages
from sys import argv

# 3rd party packages

# local packages

def remove_zeroes(sequence):
    s = [i for i in sequence if i != '0']
    return s

def is_empty(sequence):
    if not sequence:
        return True
    else:
        return False

def remove_first_element(sequence):
    n = sequence[0]
    sequence.remove(n)

    return n, sequence

def is_n_greater(n, sequence):
    if int(n) > len(sequence):
        return False
    else:
        return True

def subtract_from_n(n, sequence):
    new_sequence = []
    for i in range(int(n)):
        new_sequence.append(int(sequence[i]) - 1)

    return new_sequence

if __name__ == "__main__":
    
    algorithm = True
    user_input = list(input('Provide a sequence of numbers: '))
    
    #clean input of ' '
    sequence = [i for i in user_input if i != ' ']
    
    while algorithm:
        # step 1: remove zeroes
        sequence = remove_zeroes(sequence)

        # step 2: check if empty, return True
        if is_empty(sequence):
            print('True')
            break

        # step 3: sort in descending order
        sequence.sort(reverse=True)
        
        # step 4: remove first element in list and return as list of N and new list
        n, sequence = remove_first_element(sequence)
        
        # step 5: check if N is greater than the len of remaining list, return False
        if not is_n_greater(n, sequence):
            print('False')
            break

        # step 6: substract 1 from N elements in the list (left to right)
        sequence = subtract_from_n(n, sequence)