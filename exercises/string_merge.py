__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" String Merge:
Given two words and a letter, return a single word that's a combination of both words, merged at the point where the given letter first appears in each word. The returned word should have the beginning of the first word and the ending of the second, with the dividing letter in the middle. You can assume both words will contain the dividing letter.
    Examples

    ("hello", "world", "l")       ==>  "held"
    ("coding", "anywhere", "n")   ==>  "codinywhere"
    ("jason", "samson", "s")      ==>  "jasamson"
    ("wonderful", "people", "e")  ==>  "wondeople"

Started: Feb 14th, 2025 @ 5:20am ET
Intervals: 1
Ended: Feb 14th, 2025 @ 5:31am ET
"""

def merge_strings(strings: list) -> str:
    merged_string = ''
    first_string, second_string, join_letter = strings[0], strings[1], strings[2]
    
    # get position of split letter so we can slice there
    first_index = first_string.index(join_letter)
    second_index = second_string.index(join_letter)

    # slice them up
    first_string = first_string[:first_index]
    second_string = second_string[second_index + 1:]
    
    # merge them
    merged_string = first_string + join_letter + second_string

    return merged_string


if __name__ == "__main__":
    #strings = ["hello", "world", "l"]
    strings = ["coding", "anywhere", "n"]
    
    merged_string = merge_strings(strings)
    print(merged_string)