__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Robot Path: https://cses.fi/problemset/task/1742/


Example:
    Input:
    5
    U 2
    R 3
    D 1
    L 5
    U 2

    Output:
    9


Started: Jan 25, 2024 @ 6:40am ET
Intervals: 1
Ended: Jan 25, 2024 @ 7:10am ET
"""
from sys import argv
import json

def is_visited(visited_coordinates: list, current_coordinates: set) -> bool:
    if current_coordinates in visited_coordinates:
        return True
    else:
        return False

#TODO: implement is_visited check
def move_robot(robot_commands: dict) -> int:
    move_count = 0
    x, y = 0, 0
    visited_coordinates = [(0, 0)]


    for key, value in robot_commands.items():
        print(key, "->", value)
        
        if key == "U":
            y = y + value
            
            visited_coordinates.append((x, y))
            move_count += value

        elif key == "D":
            y = y - value

            visited_coordinates.append((x, y))
            move_count += value

        elif key == "L":
            x = x - value
            
            visited_coordinates.append((x, y))
            move_count += value

        elif key == "R":
            x = x + value
            
            visited_coordinates.append((x, y))
            move_count += value
        else:
            pass
        
        print(visited_coordinates)

    return move_count

if __name__ == "__main__":
    # '{"N":5, "U": 2, "R": 3, "D": 1, "L": 5, "U": 2}'
    robot_commands = json.loads(argv[1])
    
    r = move_robot(robot_commands)
    print(r)