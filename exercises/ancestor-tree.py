#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Ancestor Tree: https://old.reddit.com/r/dailyprogrammer/comments/sq3p9/4242012_challenge_43_easy/
Also: https://programmingpraxis.com/2011/03/11/lowest-common-ancestor/

Given a binary tree t and two elements of the tree, m and n, with m < n, find the lowest element of the tree (farthest from the root) that is an ancestor of both m and n.

For example, in the tree example, the lowest common ancestor of 4 and 7 is 6, the lowest common ancestor of 4 and 10 is 8, and the lowest common ancestor of 1 and 4 is 3. It is possible for an element of the tree to be its own ancestor, so the lowest common ancestor of 1 and 3 is 3, and the lowest common ancestor of 3 and 6 is 3.

Example: [8, 3, 10, 1, 6, 14, None, None, None, 4, 7, 13, None]

    ______8______
   /             \
  3__            _10
 /   \          /
1     6       _14
     / \     /
    4   7   13

Started: Nov 28, 2023 @ 5:25am ET
Intervals: 1
Ended: Nov 28, 2023 @ 5:55am ET
Comment: spent all the time getting the tree setup lol.
"""

from binarytree import build # need venv to work

def build_tree(nodes):
    binary_tree = build(nodes)
    return binary_tree

# TODO: t will be a list of nodes where 0 is root and subsequent pairs are branched leaves m and n
def find_lowest_element(t, m, n):
    if m > n:
        print('invalid elements give. m is greater than n')

    searchA = []
    searchB = []

    while m != None:
        pass



if __name__ == '__main__':
    binary_tree = build_tree([8, 
                              3, 10,
                                1, 6, 14, None,
                                None, None, 4, 7, 13, None])
    print(binary_tree)