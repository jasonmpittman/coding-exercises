__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Length Sort:
Create a sorting function which sorts numbers not by numerical order, but by number length! This means sorting numbers with the least amount of digits first, up to the numbers with the most digits.

Examples:
    numberLenSort([1, 54, 1, 2, 463, 2]) ➞ [1, 1, 2, 2, 54, 463]
    numberLenSort([999, 421, 22, 990, 32]) ➞ [22, 32, 999, 421, 990]
    numberLenSort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]) ➞ [9, 8, 7, 6, 5, 4, 2, 1, 3, 31]


Started: April 23, 2024 @ 5:00am ET
Intervals: 1
Ended: April 23, 2024 @ 5:17am ET
"""
from sys import argv

def sort_by_length(array: list, mode="default") -> list:
    sorted_array = []
    i = 0

    # finished at 5:21 after reading about sorted()
    if mode == "optimized":
        return sorted(array, key=len)

    # finished this @ 5:17
    if mode == "default":
        for a in array:
            print(a)
            if len(sorted_array) == 0:
                sorted_array.append(array[i])
                i += 1
            elif len(a) >= len(sorted_array[-1]):
                print("appending ", a)
                sorted_array.append(a)
                i += 1
            else:
                print("pre-pending ", a)
                sorted_array.insert(0, a)
                i += 1

        return sorted_array

if __name__ == "__main__":
    array = argv[1].split(',') # 1,54,1,2,463,2     999,421,22,990,32

    sorted_array = sort_by_length(array, mode="optimized")
    print(sorted_array)