__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Target Sum:
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

Examples:
    twoSum([1, 2, 3], 4) // returns [0, 2] or [2, 0]
    twoSum([3, 2, 4], 6) // returns [1, 2] or [2, 1]

Started: June 15, 2024 @ 7:00am ET
Intervals: 1
Ended: June 15, 2024 @ 7:07am ET
"""
from sys import argv

def sum_target(array: list, target: int) -> list:

    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == target and array[j] != array[i]:
                return array.index(array[i]), array.index(array[j])

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))
    target = int(argv[2])

    result = sum_target(array, target)
    print(result)