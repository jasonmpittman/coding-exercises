__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = "Easy"

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Start: 5:20am
End: 5:29
"""

from sys import argv

def main(strings: list) -> str:
    i = 0
    prefix = ""
    
    for _ in strings[0]:
        if strings[i][i] == strings[1][i] and strings[0][i] == strings[2][i]:
            prefix = prefix + strings[0][i]
            i += 1
        else:
            break

    return prefix

if __name__ == "__main__":
    strings = argv[1].split(',') #  flower,flow,flight
    result = main(strings)

    print(result)