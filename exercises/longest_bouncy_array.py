__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Longest Bouncy Subarray:
Write a function to output the longest strict bouncy subarray from a given array.

In the case of having more than one bouncy subarray of same length, it should be output the subarray with its first term of lowest index in the original array.

Examples:
    arr = [7,9,6,10,5,11,10,12,13,4,2,5,1,6,4,8]
    longest_bouncy_list(arr) === [7,9,6,10,5,11,10,12] 

Started: May 15, 2024 @ 4:35am ET
Intervals: 1
Ended: May 15, 2024 @ 5:05am
"""
from sys import argv

def is_nonincreasing(number: list) -> bool:
    # 987542 is nonincreasing (true)

    # naive approach to testing if number is descending order sorted
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            nonincreasing = True
        else:
            nonincreasing = False
            break
    
    return nonincreasing

def is_nondecreasing(number: list) -> bool:
    # 12345 is nondecreasing (true)
    
    # naive approach to testing if number is ascending order sorted
    for i in range(len(number) - 1):
        if number[i] < number[i + 1]:
            nondecreasing = True
        else:
            nondecreasing = False
            break
    
    return nondecreasing

#TODO: need to find 'longest'...function finds all bouncy of len = k
def find_longest_bouncy(array: list, k: int) -> list:
    bouncy_subarrays = []
    head = 0
    tail = k + 1

    while tail <= len(array): 
        # if both is_ are false, number is bouncy
        subarray = array[head:tail]
        #print(subarray)
        
        if not is_nondecreasing(subarray) and not is_nonincreasing(subarray):
            bouncy_subarrays.append(subarray)
        
        head += 1
        tail += 1
    
    return bouncy_subarrays

if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 7,9,6,10,5,11,10,12,13,4,2,5,1,6,4,8 7
    k = int(argv[2])

    bouncy_subarrays = find_longest_bouncy(array, k)
    print(bouncy_subarrays)

    #print(is_nondecreasing([7,9,6,10,5,11,10,12]))
    #print(is_nonincreasing([7,9,6,10,5,11,10,12]))
