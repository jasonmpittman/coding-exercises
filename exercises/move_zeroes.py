__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Move Zeroes:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

Example:
    moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

Started: June 10, 2024 @ 4:40am ET
Intervals: 1
Ended: June 10, 2024 @ 4:47am ET
"""

def move_zeroes(array: list) -> list:
    for element in array:
        if element == 0:
            index = array.index(element)
            array.append(0)
            del array[index]
    
    print(array)


if __name__ == "__main__":
    array = ["false",1,0,1,2,0,1,3,"a"]

    move_zeroes(array)