__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Alphabet Wars- Airstrike:

Write a function that accepts a fight string which consists of only small letters and * which represents a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, and when the right side wins return Right side wins!. In other cases, return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3 
 b - 2
 s - 1

The right side letters and their power:

 m - 4
 q - 3 
 d - 2
 z - 1

The other letters don't have power and are only victims.
The * bombs kill the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );

Example (Input --> Output)

    "s*zz"           --> "Right side wins!"
    "*zd*qm*wp*bs*"  --> "Let's fight again!"
    "zzzz*s*"        --> "Right side wins!"
    "www*www****z"   --> "Left side wins!"


Started: Feb 13, 2025 @ 7:05am ET
Intervals: 1
Ended: Feb 13, 2025 @ 7:35am ET
"""

def drop_bomb(fight: str) -> str:
    pass


if __name__ == "__main__":
    pass
