__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Climbing Stairs:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Started: May 01, 2024 @ 3:20am ET
Intervals: 1
Ended: May 01, 2024 @ 3:45am ET
"""
from sys import argv

def climb_stairs(n: int, steps = []):
    # Base cases
    if n == 0:
        print(' + '.join(str(step) + ' step' for step in steps))
        return 1
    elif n == 1:
        steps.append(1)
        print(' + '.join(str(step) + ' step' for step in steps))
        steps.pop()
        return 1
    
    # Recursive cases
    steps.append(1)
    ways_without_two_steps = climb_stairs(n - 1, steps)
    steps.pop()
    
    steps.append(2)
    ways_with_two_steps = climb_stairs(n - 2, steps)
    steps.pop()
    
    return ways_without_two_steps + ways_with_two_steps

if __name__ == "__main__":
    n = int(argv[1])

    result = climb_stairs(n)
    print(result)
