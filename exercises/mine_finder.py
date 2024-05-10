__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Mine Finder:
Write a function mineLocation/MineLocation that accepts a 2D array, and returns the location of the mine. The mine is represented as the integer 1 in the 2D array. Areas in the 2D array that are not the mine will be represented as 0s. 

Examples:
    mineLocation( [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] ) => returns [0, 0]
    mineLocation( [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] ) => returns [1, 1]
    mineLocation( [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] ) => returns [2, 1]

Started: May 10, 2024 @ 4:10am ET
Intervals: 1
Ended: May 10, 2024 @ 4:17am 
"""

def find_mine(minefield: list) -> list:
    coordinates = []

    for i in range(len(minefield)):
        for j in range(len(minefield[i])):
            if minefield[i][j] == 1:
                coordinates.append(i) 
                coordinates.append(j)
                #break # uncomment here if we want to stop after finding a single mine

    return coordinates

if __name__ == "__main__":
    minefield = [ [0, 0, 0], [0, 1, 0], [0, 1, 0] ] # [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ]

    location = find_mine(minefield)
    print(location)