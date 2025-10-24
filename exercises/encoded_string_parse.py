__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function which takes in an encoded string and returns a dictionary according to the following example:
Examples

parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}

Start: 07:00am
End: 07:30am
Cycles: 1
"""
import re
from sys import argv

def parse_code(encoded_string: str) -> dict:

    split_string = encoded_string.split('0')
    string_list = list(filter(lambda a: a != '', split_string))
    
    parsed_code = {
        'first_name': string_list[0],
        'last_name': string_list[1],
        'id': string_list[2]
    }


    return parsed_code

if __name__ == "__main__":
    encoded_string = argv[1]

    result = parse_code(encoded_string)
    print(result)

