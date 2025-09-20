__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
A Fibonacci string is a precedence of the Fibonacci series. It works with any two characters of the English alphabet (as opposed to the numbers 0 and 1 in the Fibonacci series) as the initial items and concatenates them together as it progresses in a similar fashion as the Fibonacci series.
Examples

fib_str(3, ["j", "h"]) ➞ "j, h, hj"

fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"

fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"

Start: 5:00am
End: 5:30:am
Cycles: 1
"""
import sys

def build_substring(length: int, first_letter: str, second_letter: str) -> str:
    substring = ''

    if length == 0:
        substring = first_letter
        return substring
    elif length == 1:
        substring = second_letter
        return substring
    else:
        for i in range(1, length + 1):
            if i % 2 != 0:
                substring += second_letter 
            else:
                substring += first_letter   #   more correctly, we should += substring when len >= 2
        return substring


if __name__ == "__main__":
    generations = int(sys.argv[1])
    first_letter = sys.argv[2]
    second_letter = sys.argv[3]
    fib_string = []
    first = True
    i = 0

    while i < generations:
        substring = build_substring(i, first_letter, second_letter)
        fib_string.append(substring)

        i += 1
    
    print(fib_string)