__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" String Average:
You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"

Started: Feb 17, 2025 @ 7:25am ET
Intervals: 1
Ended: Feb 17, 2025 @ 7:55am ET
"""

def average_string(number_string: str) -> int:
    average = 0

    numbers = number_string.split(' ')
    for number in numbers:
        average += int(number)

    return average // len(numbers)

if __name__ == "__main__":
    number_string = "0 9 5 2"

    result = average_string(number_string)
    print(result)