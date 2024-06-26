__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


""" Water Ballooon:
Once a water balloon pops, is soaks the area around it. The ground gets drier the further away you travel from the balloon.

The effect of a water balloon popping can be modeled using an array. Create a function that takes an array which takes the pre-pop state and returns the state after the balloon is popped. The pre-pop state will contain at most a single balloon, whose size is represented by the only non-zero element.

Examples
    pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
    pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
    pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
    pop([0]) ➞ [0]

Started: April 20, 2024 @ 6:05am ET
Intervals: 1
Ended: April 20, 2024 @ 6:16am ET
"""
from sys import argv


def pop_balloon(array: list) -> list:
    size = len(array)
    center = len(array) // 2
    effect = 1

    for i in range(1, center):
        array[i] += effect
        effect += 1
    
    for i in range(center + 1, size):
        effect -= 1
        array[i] += effect
    
    return array


if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 0,0,0,0,4,0,0,0,0 0,   0,2,0,0

    print(pop_balloon(array))
