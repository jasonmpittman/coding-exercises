__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that gets every pair of numbers from an array that sums up to eight and returns it as an array of pairs (sorted ascendingly). See the following examples for more details.
Examples

sums_up([1, 2, 3, 4, 5]) ➞ {"pairs": [[3, 5]]}

sums_up([1, 2, 3, 7, 9]) ➞ {"pairs": [[1, 7]]}

sums_up([10, 9, 7, 2, 8]) ➞ {"pairs": []}

sums_up([1, 6, 5, 4, 8, 2, 3, 7]) ➞ {"pairs": [[2, 6], [3, 5], [1, 7]]}
# [6, 2] first to complete the cycle (to sum up to 8)
# [5, 3] follows
# [1, 7] lastly
# the pair that completes the cycle is always found on the left
# [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise.

Start: 06:50am
End: 07:20:am
Cycles: 1
"""



