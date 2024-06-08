__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Previous Divide:
Take a number and check each digit if it is divisible by the digit on its left checked and return an array of booleans.

The booleans should always start with false becase there is no digit before the first one.

Examples
    73312        => [false, false, true, false, true]
    2026         => [false, true, false, true]
    635          => [false, false, false]

*** Remember 0 is evenly divisible by all integers but not the other way around ***

Started: June 08, 2024 @ 5:20am ET
Intervals: 1
Ended: June 08, 2024 @ 5:34am ET
"""
from sys import argv

def divide_previous(number: str) -> list:
    is_divisble = ['false']
    numbers = [int(x) for x in number] # why doesn't this cast to int work?
    

    for i in range(1, len(number)):
        # check for division by zero and skip
        if int(number[i - 1]) == 0:
            is_divisble.append('false')
            continue

        # check if n % n - 1 == 0
        if int(number[i]) % int(number[i - 1]) == 0:
        # if so, add true to list
            is_divisble.append('true')
        else:
            is_divisble.append('false')
    
    return is_divisble
    

if __name__ == "__main__":
    number = argv[1]

    results = divide_previous(number)
    print(results)