__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Josephus Problem:
Consider a game where there are n children (numbered 1,2,...,n) in a circle. During the game, every other child is removed from the circle until there are no children left. In which order will the children be removed?

Input:
The only input line has an integer n.

Output
Print n integers: the removal order.

Examples:
    Input:
    7

    Output:
    2 4 6 1 5 3 7

Started: April 12, 2024 @ 6:30am ET
Intervals: 1
Ended: April 12, 2024 @ 6:46am ET
"""
from sys import argv

def remove_children(number_of_children: int) -> list:
    order_of_remove = []
    circle = [x for x in range(1, number_of_children + 1)]
    print(circle)

    order_of_remove.append(circle[1::2])
    del circle[1::2]
    order_of_remove.append([x for x in circle])

    print(order_of_remove)

if __name__ == "__main__":
    number_of_children = int(argv[1])

    remove_children(number_of_children)