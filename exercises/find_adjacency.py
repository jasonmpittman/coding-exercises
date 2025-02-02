__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Find Adjacent Nodes
For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. In the example given above, nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.

We can encode graphs using an adjacency matrix. An adjacency matrix for a graph with "n" nodes is an "n * n" matrix where the entry at row "i" and column "j" is a 0 if nodes "i" and "j" are not adjacent, and 1 if nodes "i" and "j" are adjacent.

[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

  - Nodes 0,1 should return True.
  - Nodes 0,2 shuold return False.

  """

def is_adjacent(matrix, row, column) -> bool:
    
    if matrix[row][column] == 1:
        return True
    else:
        return False



if __name__ == '__main__':
    matrix = [
      [ 0, 1, 0, 0 ],
      [ 1, 0, 1, 1 ],
      [ 0, 1, 0, 1 ],
      [ 0, 1, 1, 0 ]
    ]

    print(is_adjacent(matrix, 0, 1))
