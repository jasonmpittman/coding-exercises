__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.

Examples
    is_harshad(75) ➞ False
    # 7 + 5 = 12
    # 75 is not exactly divisible by 12
    
    is_harshad(171) ➞ True
    # 1 + 7 + 1 = 9
    # 9 exactly divides 171
    
    is_harshad(481) ➞ True
    is_harshad(89) ➞ False
    is_harshad(516) ➞ True
    is_harshad(200) ➞ True

Start: 6:00am
End: 6:08:am
Cycles: 1
"""
from sys import argv

def is_harshad(number: str) -> bool:
    total = 0
    numbers = list(number)
    
    for n in numbers:
        total += int(n)

    if int(number) % total == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    numbers = argv[1]

    result = is_harshad(numbers)
    print(result)

