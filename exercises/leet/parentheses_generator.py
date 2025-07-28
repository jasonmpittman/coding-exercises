__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = "Medium"

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

Start: 8:20am
End: 8:31am 
"""
from sys import argv

def main(n: int) -> list:
    combinations = []

    #   TODO: partial solution...just not feeling it today
    def backtrack(current_string, open_count, closed_count):
        if len(current_string) == 2 * n:
            combinations.append(current_string)
            return
    
        if open_count < n:
            backtrack(current_string + "(", open_count + 1, closed_count)
        
        if closed_count < n:
            backtrack(current_string + ")", open_count, closed_count + 1)
    
    backtrack("", 0, 0)
    return combinations


if __name__ == "__main__":
    n = int(argv[1])

    result = main(n)
    print(result)