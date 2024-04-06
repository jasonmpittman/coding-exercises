__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Rotor Lock: https://codeforces.com/problemset/problem/1703/C


Started: April 06, 2024 @ 5:55am ET
Intervals: 1
Ended: April 06, 2024 @ 6:19am ET
"""
from sys import argv


if __name__ == "__main__":
    number_of_rotors = int(argv[1])
    current_rotors = list(map(int, argv[2].split(',')))
    moves = []
    rotor = -1
    
    print("The current lock is: ", current_rotors)


    while "q" not in moves:
        rotor += 1
        
        moves = input("move: ").split(',') 
        
        for move in moves:
            if move == 'D':
                # rotate rotor down if 9 go to 0
                if current_rotors[rotor] == 9:
                    current_rotors[rotor] = 0
                else:
                    current_rotors[rotor] += 1
                
            if move == 'U':
                # rotate rotor up if 0 go to 9
                if current_rotors[rotor] == 0:
                    current_rotors[rotor] = 9
                else:
                    current_rotors[rotor] -= 1
    
    print("The updated lock is: ", current_rotors)