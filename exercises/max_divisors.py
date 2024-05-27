__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Max Divisors:
Find the integer from a to b (included) with the greatest number of divisors. For example:

divNum(15, 30)   ==> 24
divNum(1, 2)     ==> 2
divNum(0, 0)     ==> 0
divNum(52, 156)  ==> 120

If there are several numbers that have the same (maximum) number of divisors, the smallest among them should be returned. Return the string "Error" if a > b.

Started: May 27, 2024 @ 6:00am ET
Intervals: 1
Ended: May 27, 2024 @ 6:30am ET
"""
from sys import argv

def find_max_divisors(a: int, b: int) -> int:
    def count_divisors(n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count

    max_divisors = 0
    number_with_max = a

    for number in range(a, b + 1):
        divisors_count = count_divisors(number)
        if divisors_count > max_divisors:
            max_divisors = divisors_count
            number_with_max = number

    return number_with_max, max_divisors

if __name__ == "__main__":
    a = int(argv[1])
    b = int(argv[2])

    divisors = find_max_divisors(a, b)
    print(divisors)


