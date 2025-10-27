__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 97=4782969. Also, please take 0^0 to be 1.

You may assume that the input will always be valid.

Examples
    lastDigit 4 1             `shouldBe` 4
    lastDigit 4 2             `shouldBe` 6
    lastDigit 9 7             `shouldBe` 9
    lastDigit 10 (10^10)      `shouldBe` 0
    lastDigit (2^200) (2^300) `shouldBe` 6

Start: 07:10pm
End: 07:18pm
Cycles: 1
"""
from sys import argv

def find_last_digit(a: int, b: int) -> int:
    power = a**b

    return power % 10 # mod 10 always returns last digit of a number

if __name__ == "__main__":
    a, b = int(argv[1]), int(argv[2])

    result = find_last_digit(a, b)
    print(result)



