__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Flatten Arrays:

write an algorithm that flatten an arrays structure to 2 levels. It means that each array under the second level will be merge to its parent. Only two levels are kept.

Empty arrays are ignored.

array = [1, [2, 3], [4, 5, [6, 7, 8], 9, 10, [11, [12, [13, 14], 15], 16], 17], 18];
return [1,[2,3],[4,5,6,7,8,9,10,11,12,13,14,15,16,17], 18]

array = [1,[2, 3, [], [4, [], 5]]]
return [1,[2,3,4,5]]


Started: Mar 4th, 2025 @ 9:00am ET (estimated)
Intervals: 1
Ended: Mar 4th, 2025 @ 9:30am ET
"""

new_array = []

def is_list(array: list) -> bool:
    if isinstance(array, list) is True:
        return True
    else:
        return False

#TODO: we're overflattening here...need to stop the recursion at 2 deep and just remove empty nested lists
def flatten_array(array: list) -> list:
    
    for a in array:
        if is_list(a):
            #print(a)
            flatten_array(a)
        else:
            new_array.append(a)

    return new_array


if __name__ == "__main__":
    array = [1, [2, 3], [4, 5, [6, 7, 8], 9, 10, [11, [12, [13, 14], 15], 16], 17], 18] #[1,[2, 3, [], [4, [], 5]]] 

    result = flatten_array(array)
    print(result)