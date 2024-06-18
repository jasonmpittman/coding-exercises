__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Geometric Sum:

geometric_sequence_sum(a, r, n), which will help you compute a geometric progression/series.

The parameters provided are as follows:

    a is the first term
    r is the common ratio
    n is the amount of terms

Example:
    geometric_sequence_sum(2, 3, 5) should return 242.

Started: June 18, 2024 @ 3:40am ET
Intervals: 1
Ended: June 18, 2024 @ 3:51am ET
"""
from sys import argv

def compute_geometric_sum(a: int, r: int, n: int) -> int:
    sequence = [a]
    
    for i in range(0, n - 1):
        t = sequence[i] * r
        sequence.append(t)

    print(sequence, sum(sequence))

if __name__ == "__main__":
    a = int(argv[1])
    r = int(argv[2])
    n = int(argv[3])

    compute_geometric_sum(a, r, n)