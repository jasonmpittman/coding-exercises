__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Elimination:
In this Kata you will be given an array (or another language-appropriate collection) representing contestant ranks. You must eliminate contestant in series of rounds comparing consecutive pairs of ranks and store all initial and intermediate results in an array.

During one round, the lowest rank of a pair is eliminated while the highest proceeds to the next round. This goes on until one contestant only is left. If the number of contestants is odd, the last one of the current array becomes the first of the next round.

At the end of the competition, return the results of all the rounds in the form of array of arrays.

Example:

input = [9, 5, 4, 7, 6, 3, 8, 2];

output = [
  [9, 5, 4, 7, 6, 3, 8, 2],  // first round is initial input
  [9, 7, 6, 8],              // results of 9 vs 5, 4 vs 7, 6 vs 3, and 8 vs 2 
  [9, 8],                    // results of 9 vs 7 and 6 vs 8
  [9]                        // results of 9 vs 8
];


Started: June 09, 2024 @ 7:35am ET
Intervals: 1
Ended: June 09, 2024 @ 7:52am ET
"""
from sys import argv

def elimination(array: list) -> list:
    new_array = []
    
    if len(array) > 1:
        
        for i in range(0,len(array) - 1,2):
            if array[i] > array[i + 1]:
                print('fight: ', array[i], array[i+1])
                new_array.append(array[i])
        #print(new_array)    
        elimination(new_array)
    else:
        print(array)
        


if __name__ == "__main__":
    array = list(map(int, argv[1].split(','))) # 9,5,4,7,6,3,8,2

    elimination(array)
    