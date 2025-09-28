
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that takes in an array of grass heights and a variable sequence of lawn mower cuts and outputs the array of successive grass heights.

If after a cut, any single element in the array reaches zero or negative, return "Done" instead of the array of new heights.

A demo:

cutting_grass([3, 4, 4, 4], 1, 1, 1) ➞ [[2, 3, 3, 3], [1, 2, 2, 2], "Done"]

# 1st cut shaves off 1: [3, 4, 4, 4] ➞ [2, 3, 3, 3]
# 2nd cut shaves off 1: [2, 3, 3, 3] ➞ [1, 2, 2, 2]
# 3rd cut shaves off 1: [1, 2, 2, 2]➞ [0, 1, 1, 1], but one element reached zero so we return "Done".

Examples
    cutting_grass([4, 4, 4, 4], 1, 1, 1, 1)
    ➞ [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], "Done"]

    cutting_grass([5, 6, 7, 5], 1, 2, 1)
    ➞ [[4, 5, 6, 4], [2, 3, 4, 2], [1, 2, 3, 1]]

    cutting_grass([8, 9, 9, 8, 8], 2, 3, 2, 1)
    ➞ [[6, 7, 7, 6, 6], [3, 4, 4, 3, 3], [1, 2, 2, 1, 1], "Done"]

    cutting_grass([1, 0, 1, 1], 1, 1, 1) ➞ ["Done", "Done", "Done"]

Start: 12:50am
End: 01:20:am
Cycles: 1
"""

