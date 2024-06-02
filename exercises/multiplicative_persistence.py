__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Persistence:
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):
    39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
    999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
    4 --> 0 (because 4 is already a one-digit number, there is no multiplication)

Started: June 02, 2024 @ 6:30am ET
Intervals: 1
Ended: June 02, 2024 @ 6:50am ET
"""
from sys import argv

def multiply(number: int) -> int:
    result = 1
    
    for digit in str(number):
        result *= int(digit)
    
    return result

def multiplicative_persistence(number: int):
    if number < 10:
        return 0
    
    count = 0
    while number > 10:
        number = multiply(number)
        count += 1
    
    return count

if __name__ == "__main__":
    number = int(argv[1])

    persistence = multiplicative_persistence(number)
    print(persistence)