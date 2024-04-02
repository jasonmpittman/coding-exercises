__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Dictionary Inversion:
Write a function that inverts the keys and values of an object.

Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }

Started: April 02, 2024 @ 3:55am ET
Intervals: 1
Ended: April 02, 2024 @ 4:01am ET
"""

def invert_dictionary(my_dict: dict, mode='short') -> dict:
    
    if mode == 'short':
        inverted_dict = dict((v,k) for k,v in my_dict.items())
    elif mode == 'long':
        inverted_dict = {}
        for k,v in my_dict.items():
            inverted_dict[v] = k

    return inverted_dict

if __name__ == "__main__":
    my_dict = { "zebra": "koala", "horse": "camel" }
    inverted_dict = invert_dictionary(my_dict, mode='short')

    print(inverted_dict)