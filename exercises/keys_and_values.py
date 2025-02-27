__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Keys and Values:
Complete the keysAndValues function so that it takes in an object and returns the keys and values as separate arrays.

Example:
    keysAndValues({a: 1, b: 2, c: 3}) // should return [['a', 'b', 'c'], [1, 2, 3]]


Started: Feb 28th, 2025 @ 6:25am ET (estimated)
Intervals: 1
Ended: Feb 28th, 2025 @ 6:40am ET
"""

def get_keys_and_values_comprehension(d: dict) -> list:
    keys_and_values = []
    keys_and_values.append([key for key in d.keys()])
    keys_and_values.append([value for value in d.values()])

    print(keys_and_values)

def get_keys_and_values(d: dict) -> list:
    keys_and_values = [[],[]]

    for key, value in d.items():
        keys_and_values[0].append(key)
        keys_and_values[1].append(value)
    
    return keys_and_values

if __name__ == "__main__":
    d = {'a': 1, 'b': 2, 'c':3}

    # naive method
    keys_and_values = get_keys_and_values(d)
    print(keys_and_values)

    #comprehesion method
    get_keys_and_values_comprehension(d)




