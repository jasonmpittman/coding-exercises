__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" String Sum:
Write a function that takes a string containing a mixture of integers and non-integer characters and returns the sum of all the numbers found in the string. Numbers can be separated by non-numeric characters.

Expected Behavior:

    The function should return an integer that is the sum of all numbers found in the input string.
    If there are no numbers in the string, the function should return 0.

Example:

    Input: "Hello123world45 67"
    Output: 235 (Since 123 + 45 + 67 = 235)

    
Started: Dec 27, 2023 @ 6:30am ET
Intervals: 1
Ended: Dec 27, 2023 @ 7:00am ET
"""
from sys import argv 

# TODO: fix bug where last elif doesn't trigger because of end of string
def sum_numbers_in_string(str):
    integers = ['0', '1', '2', '3', '4' ,'5' ,'6' ,'7', '8' ,'9']
    sum = 0
    t = ''

    for s in str: # Hello123world45 67
        print(s)
        
        if s in integers:
            t = t + s
        elif t != '':
            print(t)
            sum += int(t)
            t = ''  

    return sum


if __name__ == '__main__':
    str = argv[1] # this works if there's a space at the end of argv
    print(sum_numbers_in_string(str))