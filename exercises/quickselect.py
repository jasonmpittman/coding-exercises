__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Quickselect:
Quickselect is a selection algorithm to find the k'th smallest element in an unordered list. It is closely related to the Quicksort sorting algorithm. Like Quicksort, it is efficient traditionally and offers good average-case performance, but has a poor worst-case performance.


For example,
Input: [7, 4, 6, 3, 9, 1]
k = 2  
Output: kth smallest array element is 3    

Input: [7, 4, 6, 3, 9, 1] 
k = 1  
Output: kth smallest array element is 1 


note: for Mar 02...doing now because travel
Started: Mar 01, 2024 @ 2:30pm ET
Intervals: 1
Ended: Marc 01, 2024 @ 3:00pm ET
"""
from sys import argv

def partition(numbers: list, left: int, right: int) -> list:
    pass

# TODO: basic pseudo code here only
def quickselect(numbers: list, left: int, right: int, k: int) -> int:
    if left == right:
        return numbers[left]
    
    pivot = partition(numbers, left, right)

    if k == pivot:
        return numbers[k]
    elif k < pivot:
        right = numbers[:pivot - 1]
    else:
        left = numbers[pivot + 1]

if __name__ == "__main__":
    numbers = list(map(int, argv[1].split(','))) # 7,4,6,3,9,1 2
    k = int(argv[2])

    print(numbers)