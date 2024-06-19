__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Fisher-Yates Shuffle:
Fisher–Yates shuffle is an algorithm to generate random permutations. It takes time proportional to the total number of items being shuffled and shuffles them in place. The algorithm swaps the element at each iteration at random among all remaining unvisited indices, including the element itself.

Here’s the complete algorithm:
— To shuffle an array ‘a’ of ‘n’ elements:
for i from n-1 down to 1 do     
    j = random integer such that 0 <= j <= i
    exchange a[j] and a[i] 


Started: June 19, 2024 @ 6:05am ET
Intervals: 1
Ended: June 19, 2024 @ 6:12am ET
"""
from sys import argv
from random import randrange

def shuffle(array: list) -> list:

    for i in reversed(range(1, len(array) - 1)):
        j = randrange(i + 1)
        array[i], array[j] = array[j], array[i]

    return array

if __name__ == "__main__":
    array = list(map(int, argv[1].split(',')))

    shuffled_array = shuffle(array)
    print(shuffled_array)

