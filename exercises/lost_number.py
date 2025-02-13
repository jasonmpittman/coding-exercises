__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Lost Number:
An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, then the remaining numbers were mixed. Find the number that was deleted.

Example:

    The starting array sequence is [1,2,3,4,5,6,7,8,9]
    The mixed array with one deleted number is [3,2,4,6,7,8,1,9]
    Your function should return the int 5.

If no number was deleted from the starting array, your function should return the int 0.

Started: June 01, 2024 @ 7:05am ET
Intervals: 1
Ended: June 01, 2024 @ 7:13am ET
"""

def find_lost_number(source_list: list, mixed_list: list) -> int:
    lost_number = set(source_list).difference(set(mixed_list))

    return lost_number

if __name__ == "__main__":
    source_list = 1,2,3,4,5,6,7,8,9
    mixed_list = 3,2,4,6,7,8,1,9

    lost_number = find_lost_number(source_list, mixed_list)
    print(lost_number)