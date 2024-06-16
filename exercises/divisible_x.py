__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Divisible X:
give two parameters m and x, where m defines the max range starting from 1. You have to return the number of the numbers that can be multiple/divisible by x, where x is a string that consist 2 numbers and "and" or "or" example- "2 or 9"

Examples:
    from 1 to 1000, random chosen number of numbers being multiple of 2 or 9 is 556

    how_many(1000, "2 or 9") # should return 556
    how_many(1000, "2 and 9") # should return 55
    how_many(200, "10 or 10") # should return 20


Started: June 16, 2024 @ 9:10am ET
Intervals: 1
Ended: June 16, 2024 @ 9:32am ET
"""
from sys import argv


def is_divisible(a: int, b: int) -> bool:
    """Test if a is divisible by b"""
    if a % b == 0:
        return True
    else:
        return False

def count_multiples(m: int, x: str) -> int:
    """Count the number of numbers in the range 1, m divisible by x"""
    numbers = [z for z in range(1, m + 1)]
    count = 0
    multiples = x.split(' ')

    if 'or' in x:
        for n in numbers:
            if is_divisible(n, int(multiples[0])) or is_divisible(n, int(multiples[2])): #need a way to handle two digit numbers
                count += 1

    if 'and' in x:
        for n in numbers:
            if is_divisible(n, int(multiples[0])) and is_divisible(n, int(multiples[2])): #need a way to handle two digit numbers
                count += 1

    return count


if __name__ == "__main__":
    m = int(argv[1])
    x = argv[2]

    result = count_multiples(m, x)
    print(result)