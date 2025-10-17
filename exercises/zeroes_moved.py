__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

Start: 03:20am
End: 03:24:am
Cycles: 1
"""
from sys import argv

def move_zeroes(array: list) -> list:
    moved_zeroes = []
    index = 0

    for element in array:
        if element == '0':
            moved_zeroes.append(element)
        else:
            moved_zeroes.insert(index, element)
            index += 1
    
    return moved_zeroes

if __name__ == "__main__":
    array = argv[1].split(',')

    result = move_zeroes(array)
    print(result)




