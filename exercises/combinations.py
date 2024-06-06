__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Combinations:
Write a function that returns the amount of possible combinations when drawing the given amount of cards from a deck of cards.

The function must take two inputs: k is the amount of cards to draw. n the total amount of cards in the deck.

For example, a poker hand can be described as a 5-combination (k = 5) of cards from a 52 card deck (n = 52). The 5 cards of the hand are all distinct, and the order of cards in the hand does not matter. There are 2,598,960 such combinations.

The amount of combinations should be returned as an integer.

Examples
    combinations(52, 52) ➞ 1
    combinations(5, 52) ➞ 2598960
    combinations(10, 52) ➞ 15820024220

Started: June 06, 2024 @ 5:00am ET
Intervals: 1
Ended: June 06, 2024 @ 5:12am ET
"""
from sys import argv

def factorial(n: int) -> int:
    x = n - 1
    f = n
    for _ in range(n - 1):
        f = (f * x)
        x -= 1
    
    return f


def r_combination(n: int, r: int) -> int:
    """Impliments binomail coefficient as c(n,r) = n! / (r!(n - r)!)"""
    if n == r:
        return 1
    
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    nr_factoral = factorial(n - r)

    c = n_factorial / (r_factorial * nr_factoral)
    
    return int(c)



if __name__ == "__main__":
    n = int(argv[1])
    r = int(argv[2])

    result = r_combination(n, r)
    print(result)
