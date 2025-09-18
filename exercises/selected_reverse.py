__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that takes a list and a number and selectively reverse the order of the list based on the number you're given (second argument). If you're given the arguments [1,2,3,4,5,6] and 2, you would return the list [2,1, 4,3, 6,5].

Examples
    sel_reverse([1,2,3,4,5,6], 2) ➞ [2,1, 4,3, 6,5]
    sel_reverse([2,4,6,8,10,12,14,16], 3) ➞ [6,4,2, 12,10,8, 16,14]
    sel_reverse([5,7,2,6,0,4,6], 100) ➞ [6,4,0,6,2,7,5]

Start: 5:25am
End: 5:50:am
Cycles: 1
"""
import sys

def reverse_selection(array: list, n: int) -> list:

    #   If length exceeds the list length, reverse everything.
    if n >= len(array):
        array.reverse()
        return array
    
    #   If length is zero, return the original list.
    elif n == 0:
        return array
    
    else:
        subarrays = [array[i:i + n] for i in range(0, len(array), n)]
        print(subarrays)

        for subarray in subarrays:
            subarray.reverse()


        return subarrays

if __name__ == "__main__":
    array = sys.argv[1].split(',')
    n = sys.argv[2]

    reversed_array = reverse_selection(array, int(n))
    print(reversed_array)