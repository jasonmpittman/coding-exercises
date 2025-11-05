__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.

Examples
    []                   -->  0
    [1, 2, 3]            -->  3
    [1,2,[3,4]]          --> 4
    [1, 2, [3, 4, [5, 6]], 7, [8]] --> 8

Start: 6:20am
End: 06:50am
Cycles: 1
"""

def count_deep(array: list) -> int:
    count = 0

    for element in array:
        if isinstance(element, list):
            count += count_deep(element)
        else:
            count += 1

    return count

if __name__ == "__main__":
    array = [1,2,[3,4]] 
    print(array)

    result = count_deep(array)
    print(result)




