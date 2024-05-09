__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Distinct Contiguous: 
Given an array of size n, and an integer k, return the count of distinct contiguous numbers for all windows of size k. k will always be lower than or equal to n.

Example
    Input: array = {1, 2, 1, 3, 4, 2, 3}
        k = 4
    Since we have n = 7 and k = 4, we have 4 windows with 4 contiguous elements.
        
    Answer: [3,4,4,3]
    Explanation: First window is {1, 2, 1, 3}, count of distinct numbers is 3
                Second window is {2, 1, 3, 4} count of distinct numbers is 4
                Third window is {1, 3, 4, 2} count of distinct numbers is 4
                Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

Started: May 08, 2024 @ 8:05am ET
Intervals: 1
Ended: May 08, 2024 @ 8:35am ET
"""