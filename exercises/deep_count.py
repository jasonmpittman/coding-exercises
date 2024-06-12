__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Deep Count:
You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.

Examples
    []                   -->  0
    [1, 2, 3]            -->  3
    ["x", "y", ["z"]]    -->  4
    [1, 2, [3, 4, [5]]]  -->  7

Started: June 12, 2024 @ 5:35am ET
Intervals: 1
Ended: June 12, 2024 @ 5:56am ET
"""


def count_deep(array: list) -> int:
    """Returns count of all elements within an array or nested arrays"""
    count = 0

    for a in array:
        count += 1
        if isinstance(a, list):
            count += count_deep(a)

    return count

if __name__ == "__main__":
    array = ['x', 'y', ['z']] # [1, 2, [3, 4, [5]]] # [1, 2, 3] # ['x', 'y', ['z']]

    count = count_deep(array)
    print(count)
