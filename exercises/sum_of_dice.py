__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Sum of Dice:
You have n dices each one having s sides numbered from 1 to s. How many outcomes add up to a specified number k?

For example if we roll four normal six-sided dices we have four outcomes that add up to 5.

(1, 1, 1, 2) (1, 1, 2, 1) (1, 2, 1, 1) (2, 1, 1, 1)

There are 100 random tests with:

    0 <= n <= 10
    0 <= s <= 20
    0 <= k <= n * s


Started: May 05, 2024 @ 5:30am ET
Intervals: 1
Ended: May 05, 2024 @ 6:00am ET
"""
from sys import argv

def compute_outcomes(n: int, s: int, k: int) -> list:
   
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1 

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for x in range(1, min(j, s) + 1):
                dp[i][j] += dp[i - 1][j - x]
    
    return dp[n][k]

if __name__ == "__main__":
    n = int(argv[1])
    s = int(argv[2])
    k = int(argv[3])

    outcomes = compute_outcomes(n, s, k)
    print(outcomes)


