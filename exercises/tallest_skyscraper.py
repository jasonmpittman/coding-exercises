__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Tallest Skyscraper:

A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).

Example:
    [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]]

    -> 4

Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

Started: Feb 29, 2024 @ 5:00am ET
Intervals: 1
Ended: Feb 29, 2024 @ 5:12am ET
"""

def find_tallest_skyscraper(skyline: list) -> int:

    columns = [[row[i] for row in skyline] for i in range(len(skyline[0]))]

    height = max([sum(column) for column in columns])

    return height

if __name__ == "__main__":
    #skyline = [[0, 0, 0, 0], # -> 3
    #    [0, 1, 0, 0],
    #    [0, 1, 1, 0],
    #    [1, 1, 1, 1]]

    skyline = [[0, 0, 0, 0, 0, 0], # -> 4
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]]


    height = find_tallest_skyscraper(skyline)
    print(height)