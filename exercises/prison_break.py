__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Prison Break:
A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.

[1, 1, 0, 0, 0, 1, 0]

Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. You are the prisoner in the first cell. If the first cell is locked, you cannot free anyone. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.

Example:
    [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 1st cell.

    [0, 0, 1, 1, 1, 0, 1] 
    # You free the prisoner in the 3rd cell (2nd one locked).

    [1, 1, 0, 0, 0, 1, 0]
    # You free the prisoner in the 6th cell (3rd, 4th and 5th locked).

    [0, 0, 1, 1, 1, 0, 1]
    # You free the prisoner in the 7th cell - and you are done!

    freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4

Started: Jan 17, 2024 @ 4:45am ET
Intervals: 1
Ended: Jan 17, 2024 @ 5:15am ET
"""
from sys import argv

def turn_cells(cells: list) -> list:
    for index in range(len(cells)):
        if cells[index] == '1':
            cells[index] = '0'
        else:
            cells[index] = '1'

    return cells

# TODO: this works but hits an index out of range on line 53 before ending correctly
def free_prisoners(cells: list, count_freed = 0, position = 0) -> int:
    print(count_freed, position, cells) 

    # check first cell, if unlocked free and start else we're done
    i = 1
    while i < len(cells):
        if cells[position] == '1':
            count_freed += 1
            position += 1
        
            new_cells = turn_cells(cells)

            free_prisoners(new_cells, count_freed, position)
        else:
            position += 1
        
        i += 1

    return count_freed

if __name__ == '__main__':
    cells = argv[1].split(',') # 1,1,0,0,0,1,0
    print(free_prisoners(cells))