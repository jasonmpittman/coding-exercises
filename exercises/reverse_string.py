__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Reverse String:

Created for test_reverse_string challenge

"""
from sys import argv

def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    string = argv[1]
    print(reverse_string(string))
    