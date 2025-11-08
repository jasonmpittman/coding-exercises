__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
    filter_list([1,2,'a','b']) == [1,2]
    filter_list([1,'a','b',0,15]) == [1,0,15]
    filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

Start: 9:25am
End: 09:37am
Cycles: 1
"""

def filter_list(array: list) -> list:
    new_array = []
    for element in array:
        if isinstance(element, int):
            new_array.append(element)
        
    return new_array

if __name__ == "__main__":
    array = [1,2,'aasf','1','123',123]

    result = filter_list(array)
    print(result)



