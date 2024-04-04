__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Happy Numbers:
A 1 is unhappy if the digit to its left and the digit to its right are both 0s. A 0 is unhappy if the digit to its left and the digit to its right are both 1s. If a number has only one neighbor, it is unhappy if its only neighbor is different. Otherwise, a number is happy.

Write a function that takes in an array of 0s and 1s and outputs the portion of numbers which are happy. The total portion of numbers which are happy can be represented as: portion of happy numbers = (happy 0s + happy 1s) / total numbers

Examples:
    portionHappy([0, 1, 0, 1, 0]) ➞ 0
    portionHappy([0, 1, 1, 0]) ➞ 0.5
    portionHappy([0, 0, 0, 1, 1]) ➞ 1
    portionHappy([1, 0, 0, 1, 1]) ➞ 0.8

Started: April 04, 2024 @ 5:15am ET
Intervals: 1
Ended: April 04, 2024 @ 5:45am ET
"""

