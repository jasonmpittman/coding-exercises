__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
A group of n prisoners stand in a circle awaiting execution. Starting from an arbitrary position(0), the executioner kills every kth person until one person remains standing, who is then granted freedom (see examples).

Create a function that takes 2 arguments — the number of people to be executed n, and the step size k, and returns the original position (index) of the person who survives.

Examples
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

Start: 06:30am
End: 07:00:am
Cycles: 1
"""
from sys import argv

def who_goes_free(people: list, k: int) -> list:

    target = 0

    while len(people) > 1:
        number_of_people = len(people)
        shot = []

        for person in people:
            if (people.index(person) + 1 + target) % k == 0:
                shot.append(person)

            target = (number_of_people + target) % k 

        for i in people:
            if i in shot:
                people.remove(i)

    return people

if __name__ == "__main__":
    n = int(argv[1])
    k = int(argv[2])

    people = [x for x in range(n)]

    result = who_goes_free(people, k)
    print(result)

