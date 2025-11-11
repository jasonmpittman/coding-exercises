__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.
Example:

n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]

Start: 7:05am
End: 07:20am
Cycles: 1
"""
from sys import argv


def generate_triangle(n: int) -> list:
    if n <= 0:
        return []

    flattened_triangle = []
    current_row = []

    for i in range(n):
        new_row = [1] * (i + 1)  # Initialize new row with 1s
        if i > 1:
            # Calculate middle elements based on the previous row
            for j in range(1, i):
                new_row[j] = current_row[j - 1] + current_row[j]
        
        flattened_triangle.extend(new_row)
        current_row = new_row  # Update current_row for the next iteration

    return flattened_triangle

if __name__ == "__main__":
    depth = int(argv[1])

    result = generate_triangle(depth)
    print(result)




