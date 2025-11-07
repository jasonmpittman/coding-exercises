__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number. You are not allowed to use any loops (including for, for/in, while, and do/while loops).

The array will never be empty.

Examples
    [2, 452, 5, 8, 92, 46, 3, 69] equal to 676, and the average is 84.5, rounded to 85.

Start: 5:05am
End: 05:35am
Cycles: 1
"""

def average_scores(array: list, index: int = 0, current_sum: int = 0, count: int = 0) -> int:
    """ recursive function to calculate average score from a list of scores """
    if index == len(array):
        if count == 0:
            return 0
        return round(current_sum / count)
    else:
        return average_scores(array, index + 1, current_sum + array[index], count + 1)


if __name__ == "__main__":
    result = average_scores([2, 452, 5, 8, 92, 46, 3, 69])
    print(result)

