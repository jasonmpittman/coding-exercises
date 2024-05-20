__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Split Pad:
Complete the function that receives 3 arguments: n, array, padding and returns a new array that contains the result of splitting array into arrays of size n. If the last array doesn't have enough items, pad it with padding so that it becomes equal in size to the other split arrays.

Examples
    2, [1, 2, 3, 4], nil  ==>  [ [1, 2], [3, 4] ]
    2, [1, 2, 3], nil     ==>  [ [1, 2], [3, nil] ]

Started: May 20, 2024 @ 6:25am ET
Intervals: 1
Ended: May 20, 2024 @ 6:39am
"""
from sys import argv

def split_and_pad_array(n: int, array: list, padding: str) -> list:
    #get split location with offset for odd length
    if len(array) % 2 == 0:
        split = (len(array) // 2)
    else:
        split = len(array) // 2 + 1
    
    left_split = array[0:split]
    right_split = array[split:]

    #add padding if len not equal
    if len(right_split) < len(left_split):
        for i in range((len(left_split) - len(right_split))):
            right_split.append(padding)

    return left_split, right_split

if __name__ == "__main__": # 2 1,2,3,4 nil
    n = int(argv[1])
    array = argv[2].split(',')
    padding = argv[3]

    split_array = split_and_pad_array(n, array, padding)
    print(split_array)