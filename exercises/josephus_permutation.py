__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Josephus Permutation:

A group of n prisoners stand in a circle awaiting execution. Starting from an arbitrary position(0), the executioner kills every kth person until one person remains standing, who is then granted freedom (see examples).

Create a function that takes 2 arguments — the number of people to be executed n, and the step size k, and returns the original position (index) of the person who survives.

Examples:
    who_goes_free(9, 2) ➞ 2

    # Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Executed people replaced by - (a dash) for illustration purposes.
    # 1st round of execution = [0, -, 2, -, 4, -, 6, -, 8]  -> [0, 2, 4, 6, 8]
    # 2nd round = [-, 2, -, 6, -] -> [2, 6]  # 0 is killed in this round because it's beside 8 who was skipped over.
    # 3rd round = [2, -]

    who_goes_free(9, 3) ➞ 0

    # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # [0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
    # [0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
    # [0, 1, -, 6] -> [0, 1, 6]
    # [0, -, 6] -> [0, 6]
    # [0, -] -> [0]

Started: Feb 20, 2024 @ 7:50am ET
Intervals: 1
Ended: Feb 20, 2024 @ 8:10am ET
"""
from sys import argv

def generate_kill_list(length: int, step_size: int) -> list:
    kill_list = []
    limit = step_size

    while limit <= length:
        kill_list.append(limit)
        limit = limit + step_size

    return kill_list


def who_goes_free(people: list, step_size: int) -> int:
    person_freed = 0

    while len(people) > 1:
        kill_list = generate_kill_list(len(people), step_size)
        
        for kill in sorted(kill_list, reverse=True):
            del people[kill - 1]

        print(people)

    return person_freed

if __name__ == "__main__":
    people = list(map(int, argv[1].split(','))) # 0,1,2,3,4,5,6,7,8
    step_size = int(argv[2])

    person_freed = who_goes_free(people, step_size)
    print(person_freed)