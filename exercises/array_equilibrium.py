__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Array Equilibrium:

For an array A consisting n elements, index i is an equilibrium index if the sum of elements of subarray A[0…i-1] is equal to the sum of elements of subarray A[i+1…n-1]. i.e.

(A[0] + A[1] + … + A[i-1]) = (A[i+1] + A[i+2] + … + A[n-1]), where 0 < i < n-1

Similarly, 0 is an equilibrium index if A[1] + A[2] + … + A[n-1] sums to 0 and n-1 is an equilibrium index if A[0] + A[1] + … + A[n-2] sums to 0.

Example:
Input array {0, -3, 5, -4, -2, 3, 1, 0}. 
Output index 0, 3, and 7.


Started: Feb 27, 2024 @ 4:35am ET
Intervals: 1
Ended: Feb 27, 2024 @ 5:05am ET
"""
from sys import argv

def sum_left(subarray: list) -> int:
    print("Sum left: ", subarray)
    return sum(subarray)

def sum_right(subarray: list) -> int:
    print("Sum right: ", subarray)
    return sum(subarray)

def is_sum_equal(x: int, y: int) -> bool:
    if x == y:
        return True
    else:
        return False

# TODO: small bug in how 0 and size is handled...
def find_equilibriua(array: list):
    equilibriua = []
    left_subarray = 0
    right_subarray = 0
    size = len(array) - 1

    for i in range(len(array)):
        # slice left and use sum_left
        left_subarray = sum_left(array[:i])
        
        # slice right and use sum_right
        right_subarray = sum_right(array[i:size])

        # if two sums equal, append index of i to equilibria
        if is_sum_equal(left_subarray, right_subarray):
            print("Equilibriua at: ", i)
            equilibriua.append(i)

    return equilibriua

if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 0,-3,5,-4,-2,3,1,0
    
    equilibriua = find_equilibriua(array)
    print(equilibriua)