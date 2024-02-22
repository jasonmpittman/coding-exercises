__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Walk a Minefield: https://old.reddit.com/r/dailyprogrammer/comments/7d4yoe/20171114_challenge_340_intermediate_walk_in_a/

You must remotely send a sequence of orders to a robot to get it out of a minefield.

You win the game when the order sequence allows the robot to get out of the minefield without touching any mine. Otherwise it returns the position of the mine that destroyed it.

+++++++++++++
+000000000000
+0000000*000+
+00000000000+
+00000000*00+
+00000000000+
M00000000000+
+++++++++++++

The mines are represented by * and the robot by M.

The orders understandable by the robot are as follows:

    N moves the robot one square to the north
    S moves the robot one square to the south
    E moves the robot one square to the east
    O moves the robot one square to the west
    I start the the engine of the robot
    - cuts the engine of the robot

If one tries to move it to a square occupied by a wall +, then the robot stays in place.

If the robot is not started (I) then the commands are inoperative. It is possible to stop it or to start it as many times as desired (but once enough)

When the robot has reached the exit, it is necessary to stop it to win the game.


Started: Feb 22, 2024 @ 4:50am ET
Intervals: 1
Ended: Feb 22, 2024 @ 5:20am ET
"""

def move_robot(current_position, command):
    pass

if __name__ == "__main__":
    ROBOT_ON = False
    
    minefield = [
        "+++++++++++++",
        "+000000000000",
        "+0000000*000+",
        "+00000000000+",
        "+00000000*00+",
        "+00000000000+",
        "M00000000000+",
        "+++++++++++++"
    ]

    x = 6
    y = 0
    current_position = [x, y]


