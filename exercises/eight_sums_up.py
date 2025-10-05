__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that gets every pair of numbers from an array that sums up to eight and returns it as an array of pairs (sorted ascendingly). See the following examples for more details.

Examples
    sums_up([1, 2, 3, 4, 5]) ➞ {"pairs": [[3, 5]]}
    sums_up([1, 2, 3, 7, 9]) ➞ {"pairs": [[1, 7]]}
    sums_up([10, 9, 7, 2, 8]) ➞ {"pairs": []}
    sums_up([1, 6, 5, 4, 8, 2, 3, 7]) ➞ {"pairs": [[2, 6], [3, 5], [1, 7]]}
    # [6, 2] first to complete the cycle (to sum up to 8)
    # [5, 3] follows
    # [1, 7] lastly
    # the pair that completes the cycle is always found on the left
    # [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise.

Start: 06:50am
End: 07:20:am
Cycles: 1
"""
from sys import argv

def sums_up_hash(numbers: list) -> dict:
    """ Slightly different than sums_up_sorted as we test all possible combinations not just from numbers"""
    pairs = {"pairs": []}
    lookup = []
    target_sum = 8

    for number in numbers:
        #   Calculate the complement needed to reach the target_sum (i.e., target_sum - number).
        compliment = target_sum - number

        #   Check if the complement exists in the hash set. If it does, a pair is found, and you can return True.
        if compliment in lookup:
            continue

        #   If the complement is not found, add the current number to the hash set.
        if compliment not in lookup:
            lookup.append([compliment, number])
            pairs["pairs"].append([compliment, number])

    return pairs

def sums_up_sorted(numbers: list) -> dict:
    pairs = {"pairs": []}
    left_pointer = 0
    right_pointer = len(numbers) - 1
    target_sum = 8

    #   sort the list
    numbers.sort()

    #   iterate and compare
    while numbers[left_pointer] < numbers[right_pointer]:
        print(f'comparing {numbers[left_pointer]} + {numbers[right_pointer]}')

        if numbers[left_pointer] + numbers[right_pointer] == target_sum:
            pairs["pairs"].append([numbers[left_pointer], numbers[right_pointer]])
            right_pointer -= 1

        if numbers[left_pointer] + numbers[right_pointer] < target_sum:
            left_pointer += 1
        
        if numbers[left_pointer] + numbers[right_pointer] > target_sum:
            right_pointer -= 1

    return pairs

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5] # [1, 6, 5, 4, 8, 2, 3, 7] # [1, 2, 3, 7, 9] # [1, 2, 3, 4, 5]

    results = sums_up_sorted(numbers)
    print(results)

    results = sums_up_hash(numbers)
    print(results)



