__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Check Digit:
Each digit in the product number is assigned a multiplication factor. The factors are assigned from right to left, starting at 2 and counting up. For numbers longer than six digits, the factors restart at 2 after 7 is reached. The product of each digit and its factor is calculated, and the products summed. For example:

digit     :  1    6    7    7    0    3    6    2    5
factor    :  4    3    2    7    6    5    4    3    2
           ---  ---  ---  ---  ---  ---  ---  ---  ---
             4 + 18 + 14 + 49 +  0 + 15 + 24 +  6 + 10 = 140

Then the sum of the products is divided by the prime number 11. The remainder is inspected, and:

    if the remainder is 0, the check digit is also 0
    if the remainder is 1, the check digit is replaced by an uppercase X
    for all others, the remainder is subtracted from 11

Examples:
    input: "036532"

    product sum = 2*2 + 3*3 + 5*4 + 6*5 + 3*6 + 0*7 = 81
    remainder   = 81 mod 11 = 4
    check digit = 11 - 4 = 7

    output: "0365327"

Started: May 21, 2024 @ 5:50am ET
Intervals: 1
Ended: May 21, 2024 @ 6:20am
"""