__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function that returns true if it contains any duplicate argument values, and false otherwise. Any number of arguments may be passed into the function.

The arguments passed in will only be strings or numbers.

Examples:
    solution(1, 2, 3)             -->  false
    solution(1, 2, 3, 2)          -->  true
    solution('1', '2', '3', '2')  -->  true

Start: 05:25pm
End: 05:31pm
Cycles: 1
"""
from sys import argv


def solution(arguments: list) -> bool:

    unique_solution = set(arguments) #  this drops duplicates

    if len(unique_solution) < len(arguments):
        return True
    else:
        return False


if __name__ == "__main__":
    arguments = argv[1::] # take list after the 0th element which is the program name

    result = solution(arguments)
    print(result)


