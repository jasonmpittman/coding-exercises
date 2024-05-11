__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Collection Differences:
Find the difference between two collections. The difference means that either the character is present in one collection or it is present in other, but not in both. Return a sorted list with the difference.

The collections can contain any character and can contain duplicates.

Example
    A = [a, a, t, e, f, i, j]
    B = [t, g, g, i, k, f]
    difference = [a, e, g, j, k]

Started: May 11, 2024 @ 5:40am ET
Intervals: 1
Ended: May 11, 2024 @ 6:10am 
"""
from sys import argv

def find_differences(A: list, B: list, mode="set") -> list:
    differences = []

    if mode == "set": #547
        differences.append(set(A).difference(set(B)))
        differences.append(set(B).difference(set(A)))

    if mode == "naive": #549
        for a in A:
            if a not in B and a not in differences:
                differences.append(a)
        
        for b in B: 
            if b not in A and b not in differences:
                differences.append(b)

    return differences


if __name__ == "__main__":
    A = argv[1].split(',') # a,a,t,e,f,i,j t,g,g,i,k,f
    B = argv[2].split(',')

    differences = find_differences(A, B, "naive")
    print(differences)