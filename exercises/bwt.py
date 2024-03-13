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

def move_last_letter(string: str) -> list:
    """ moves last letter of string to the front of the string"""    
    strings = []
    i = 1

    while i <= len(string):
        string = string[-1] + string[0:-1]
        strings.append(string)
        
        i += 1

    return strings

def sort_string_list(strings: list) -> list:
    """ sort table of strings ascending"""
    return list(sorted(strings))

def get_last_column(strings: list) -> str:
    """ take last column of characters as bwt output"""
    characters = ""

    for i in range(len(strings)):
        characters = characters + strings[i][-1]
    
    print(characters) # nnbaaa

def transform_string(string: str) -> str:
    """ performs Burrows-Wheeler Transform on the input"""

    strings = move_last_letter(string)
    print(strings)

    sorted_strings = sort_string_list(strings)
    print(sorted_strings)

    transformed_text = get_last_column(sorted_strings)

    return transformed_text


if __name__ == "__main__":
    string = argv[1]

    result = transform_string(string)
    print(result)