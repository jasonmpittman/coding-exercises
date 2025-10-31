__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Write a function that removes digits 1234567890 from strings. 

Example 
    "abc123" -> "abc"

Start: 6:50pm
End: 07:00pm
Cycles: 1
"""
from sys import argv

def remove_digits(string: str) -> str:
    digits = "01234567890"
    clean_string = ''

    for char in string:
        if char not in digits:
            clean_string += char
        
    return clean_string

if __name__ == "__main__":
    string = argv[1]

    result = remove_digits(string)
    print(result)