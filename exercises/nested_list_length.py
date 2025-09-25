__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Python's len() method will return the number of elements in a list. For example, the list below contains 2 elements:

[1, [2, 3]]
# 2 elements, number 1 and list [2, 3]

Suppose we instead wanted to know the total number of non-nested items in the nested list. In the above case, [1, [2, 3]] contains 3 non-nested items, 1, 2 and 3.

Create a function that returns the total number of non-nested items in a nested list.

Examples
    get_length([1, [2, 3]]) ➞ 3
    get_length([1, [2, [3, 4]]]) ➞ 4
    get_length([1, [2, [3, [4, [5, 6]]]]]) ➞ 6
    get_length([1, [2], 1, [2], 1]) ➞ 5

Start: 5:10am
End: 5:35:am
Cycles: 1
"""

def get_length(array: list) -> int:
    count = 0
    for item in array:
        if isinstance(item, list):
            count += get_length(item)  #    recursively count elements in array
        else:
            count += 1  #   base 
    return count

if __name__ == "__main__":
    array = [1, [2, [3, [4, [5, 6]]]]]

    result = get_length(array)        
    
    print(result)


