__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" List Filtering:
Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
    filter_list([1,2,'a','b']) == [1,2]
    filter_list([1,'a','b',0,15]) == [1,0,15]
    filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

Started: May 04, 2024 @ 6:15am ET
Intervals: 1
Ended: May 04, 2024 @ 6:45am ET
"""
from sys import argv

def filter_numbers(element: str) -> bool:
    numbers = [str(x) for x in range(0,1000)]

    if element in numbers:
        return True
    else:
        return False

def filter_letters(element: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = [a for a in alphabet] #list(alphabet)
    
    if element in letters:
        return True
    else:
        return False 

def filter_list(the_list: list, filter_type='default') -> list:

    if filter_type == 'default':
        return list(filter(filter_letters, the_list))
    
    if filter_type == 'numeric':
        return list(filter(filter_numbers, the_list))

if __name__ == "__main__":
    the_list = argv[1].split(',')

    filtered_list = filter_list(the_list, filter_type='numeric')
    print(filtered_list)
    