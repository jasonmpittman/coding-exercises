__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Bubble Sort: 

Timed exercise to implement bubble sorting on a list of integers

Started: Feb 26, 2024 @ 6:25am ET
Intervals: 1
Ended: Feb 26, 2024 @ 6:33am ET
"""
from sys import argv

def bubble_sort(numbers: list) -> list:
    length = len(numbers)
    swapped = False

    print("Starting list is: ", numbers)

    for i in range(0, length):

        for j in range(0, length-i-1):
        
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                print("Changed list is now: ", numbers)
                swapped = True

        if swapped == False:
            break

    return numbers


if __name__ == "__main__":
    # 2,0,4,1,3
    numbers = argv[1].split(',')
    bubble_sort(numbers)