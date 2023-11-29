#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""String Compression:

Write a function that performs a basic form of string compression using the counts of repeated characters. For example, the string "aabcccccaaa" would become "a2b1c5a3". If the "compressed" string would not become smaller than the original string, your function should return the original string. The function should handle upper and lower case letters separately.

    compressString("aabcccccaaa") should return "a2b1c5a3".
    compressString("abcd") should return "abcd" (since compressing doesn't shorten it).
    compressString("AAaaBBbb") should return "A2a2B2b2" (note the case sensitivity).
    compressString("") should return "" (empty string case). x

Started: Nov 29, 2023 @ 4:45am ET
Intervals: 1
Ended: Nov 29, 2023 @ 5:15am ET    

"""

from sys import argv

# TODO: handle strings with no compression eg abcd
def compress_string(string):
    compressed_string = ""
    count = 1

    # algorithm #
    # for each c in string
    # if c is same as c + 1
    # inc count
    # else add c + count to comp str and 
    # move to next c
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            compressed_string += string[i] + str(count)
            count = 1
    compressed_string += string[i] + str(count)

    return compressed_string


if __name__ == '__main__':
    if len(argv) == 2:
        string = argv[1].strip()
        substrings = compress_string(string)
        print(substrings)
    else:
        print('""')