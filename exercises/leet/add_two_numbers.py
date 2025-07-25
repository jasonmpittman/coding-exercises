__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = "Medium"

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Start: 5:20am
End:
"""
from sys import argv

def main(a: list, b: list) -> list:
    #   reverse the input lists
    a.reverse()
    b.reverse()

    #   join and cast to int
    x = int("".join(a))
    y = int("".join(b))

    #   summation
    z = x + y

    #   reverse sum and return cast to list
    result = list(str(z))
    result.reverse()

    return result


if __name__ == "__main__":
    a = list(argv[1])
    b = list(argv[2])

    result = main(a, b)
    print(result)