__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Permutation Printing:

You are given a positive integer 𝑛

Find a permutation† 𝑝 of length 𝑛 such that there do not exist two distinct indices 𝑖 and 𝑗 (1≤𝑖,𝑗<𝑛; 𝑖≠𝑗) such that 𝑝𝑖 divides 𝑝𝑗 and 𝑝𝑖+1 divides 𝑝𝑗+1

Example:
    Input: 
        2
        4
        3
    
    Output
        4 1 2 3
        1 2 3

Started: Feb 27, 2024 @ 4:00am ET
Intervals: 1
Ended: Feb 27, 2024 @ 4:30am ET
"""
from sys import argv

def find_permutation(n: int) -> list:
    permutation = [n]  # Start with the largest integer n...i think this works?
    
    for i in range(n - 1, 0, -1):
        insert_index = 0
    
        while insert_index < len(permutation) and (i % permutation[insert_index] == 0 or permutation[insert_index] % i == 0):
            insert_index += 1
        permutation.insert(insert_index, i)
    
    return permutation    

if __name__ == "__main__":
    n = int(argv[1]) # 4 will output [2 3 4 1] i divides j but i+1 !/ j+1

    print(find_permutation(n))