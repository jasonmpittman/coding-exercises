__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Happy Number:
Given any number, we can create a new number by adding the sums of squares of digits of that number. For example, given 203, our new number is 4 + 0 + 9 = 13. If we repeat this process, we get a sequence of numbers:

203 -> 13 -> 10 -> 1 -> 1

Sometimes, like with 203, the sequence reaches (and stays at) 1. Numbers like this are called happy.

Not all numbers are happy. If we started with 11, the sequence would be:

11 -> 2 -> 4 -> 16 -> ...

This sequence will never reach 1, and so the number 11 is called unhappy.

Given a positive whole number, you have to determine whether that number is happy or unhappy.

Started: Mar 01, 2024 @ 7:30am ET
Intervals: 1
Ended: Marc 01, 2024 @ 8:00am ET
"""
from sys import argv

def sum_values(n: str):
    return sum([(int(x)**2) for x in n])

# TODO hacky af...getting infinite loop when should be False (107)
def is_happy_number(n: str) -> bool:
    value = 0
    seen = []

    
    while n != "0" and n not in seen:
        
        print("start of while for n is: ", n)
        
        if n == "1":
            print("n is 1")
            return True
        else:
            value = sum_values(n)
            seen.append(value)
            n = str(value)

        print("end of while for n is: ", n)
    
    return False
    

if __name__ == "__main__":
    n = argv[1]

    print(is_happy_number(n))