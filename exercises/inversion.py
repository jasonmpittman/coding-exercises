__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Start: 5:30am
End: 5:35am
Cycles: 1

Write a function that inverts the keys and values of a dictionary.
Examples

invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
"""

import sys


def main():
    my_dict = { "z": "q", "w": "f" }
    inverted_dict = {}

    #   for loop inversion
    for key, value in my_dict.items():
        inverted_dict[value] = key
    
    print(my_dict)
    print(inverted_dict)


    #   dictionary comprehension inverstion
    inverted_dict = {value: key for key, value in my_dict.items()}
    print(my_dict)
    print(inverted_dict)



if __name__ == "__main__":
    main()