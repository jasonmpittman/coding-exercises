__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" PassedFailed:

The challenge is to fix all of the bugs in this incredibly messy code, which the code in the image might've actually looked like (probably not)! The code given will output the same middle two lines as in the image shown above.

First parameter is the user's score.

Second parameter is the required score.

    Examples

    grade_percentage("85%", "85%") ➞ "You PASSED the Exam"

    grade_percentage("99%", "85%") ➞ "You PASSED the Exam"

    grade_percentage("65%", "90%") ➞ "You FAILED the Exam"


Started: Feb 08, 2025 @ 4:00am ET
Intervals: 1
Ended: Feb 08, 2025 @ 4:30am ET
"""

from os import wait
import sys

def grade_percentage(user_score, pass_score):
    s=''

    if int(user_score[:-1]) <= int(pass_score[:-1]):
        s = 'FAILED'
	
    if int(user_score[:-1]) >= int(pass_score[:-1]):
        s = 'PASSED'
	
    return 'You'+' '+s+' '+'the Exam'



if __name__ == "__main__":
    user_score, pass_score = sys.argv[1], sys.argv[2]
    result = grade_percentage(user_score, pass_score)

    print(result)
