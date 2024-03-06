__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Largest Function: 
Your function will be passed two functions, f and g, that don't take any parameters. Your function has to call them, and return a string which indicates which function returned the larger number.

    If f returns the larger number, return the string f.
    If g returns the larger number, return the string g.
    If the functions return the same number, return the string neither.

Examples:
    whichIsLarger(() => 5, () => 10) ➞ "g"
    whichIsLarger(() => 25,  () => 25) ➞ "neither"
    whichIsLarger(() => 505050, () => 5050) ➞ "f"


Started: Mar 06, 2024 @ 5:40am ET
Intervals: 1
Ended: Marc 06, 2024 @ 5:45am ET
"""

def f():
    return 25

def g():
    return 25

def which_is_larger(f, g) -> str:
    if f > g:
        return "f"
    elif g > f:
        return "g"
    elif f == g:
        return "neither"
    else:
        return "something went wrong"


if __name__ == "__main__":
    l = which_is_larger(f(), g())
    print(l)