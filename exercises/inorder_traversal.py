__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Inorder Traversal:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input:
		   1
		 /   \
		/	  \
	   2	   3
	  /		  / \
	 /	  	 /	 \
	4		5	  6
		   / \
		  /   \
		 7	   8

Output: [4, 2, 1, 7, 5, 8, 3, 6]

Started: April 22, 2024 @ 6:00am ET
Intervals: 1
Ended: April 22, 2024 @ 6:24am ET
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
# in-order traversal is left -> root -> right
def inorder_traversal(node):
    if node is None:
        return 

    # start on the left
    inorder_traversal(node.left)

    # visit the node
    print(node.data, end=' ')

    # go to the right
    inorder_traversal(node.right)

if __name__ == "__main__":
    #build binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    inorder_traversal(root)
    

    
      