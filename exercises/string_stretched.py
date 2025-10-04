__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function that returns True if the first string is the second string stretched, and False otherwise. A stretch is to repeat each character in a string the same number of times.

Examples
    is_stretched("pppaaannndddaaa", "panda") ➞ True
    is_stretched("sssshhiipp", "ship") ➞ False
    is_stretched("magnet", "magnet") ➞ True
    is_stretched("magneto", "magnet") ➞ False

Start: 10:25am
End: 10:55:am
Cycles: 1
"""
from sys import argv

def is_stretched(first_string: str, second_string: str) -> bool:
    stretched = False
    counts = []
    i = 0

    for second_string_letter in second_string:
        print(f'Checking second string {second_string_letter}')
        j = 0

        while first_string[i] == second_string_letter:
            print(f'Checking first string {first_string[i]}')
            j += 1
            i += 1
            print(j, i)

        counts.append(j)
        

    print(counts)

    return stretched

if __name__ == "__main__":
    first_string = argv[1]
    second_string = argv[2]

    result = is_stretched(first_string, second_string)
    print(result)


