__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Subarray Index
Write a function that looks for an array within a two-dimensional array and returns the index of the first matching element. If there is no match, your function should return -1.

Examples:
    var arrayToSearch = [[1,2],[3,4],[5,6]];
    var query = [1,2]; // => 0
    query = [5,6]; // => 2
    query = [9,2]; // => -1
    
    var arrayToSearch = [[1,2],[3,4],[5,6],[7,8,9]]; // => throw Error
    arrayToSearch = [1,2,3,4,5,6]; // => throw Error
    arrayToSearch = [[1,2],[3,4],[5,6]]; // => valid input
    var query = [1,2]; // => valid input
    query = 5; // => throw Error
    query = [9,2,1]; // => throw Error

Started: May 23, 2024 @ 6:05am ET
Intervals: 1
Ended: May 23, 2024 @ 6:35am ET
"""