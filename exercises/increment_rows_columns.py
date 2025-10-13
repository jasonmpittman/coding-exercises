__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function that takes in three parameters: r, c, i, where:

    r and c are the number of rows and columns to initialize a zero matrix.
    i represents the list of incrementing operations (+1).

And returns the resulting matrix after applying all the increment operations. Each increment operation will add 1 to the rows or columns specified in the incrementing list.

final(3, 3, ["2r", "2c", "1r", "0c"])

# Initialize a 3 x 3 matrix of zeroes.

[
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

# Apply "2r" (increment index 2 row).

[
  [0, 0, 0],
  [0, 0, 0],
  [1, 1, 1]
]

# Apply "2c" (increment index 2 column).

[
  [0, 0, 1],
  [0, 0, 1],
  [1, 1, 2]
]

# Apply "1r" (increment index 1 row).

[
  [0, 0, 1],
  [1, 1, 2],
  [1, 1, 2]
]

# Apply "0c" (increment index 0 column).
# This is the result you should return.

[
  [1, 0, 1],
  [2, 1, 2],
  [2, 1, 2]
]

Start: 06:30am
End: 07:00:am
Cycles: 1
"""