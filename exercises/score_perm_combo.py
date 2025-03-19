__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Score Permutation Combo:
We define the score of permutations of combinations, of an integer number (the function to obtain this value:sc_perm_comb) as the total sum of all the numbers obtained from the permutations of all the possible combinations of its digits. For example we have the number 348.

sc_perm_comb(348) = 3 + 4 + 8 + 34 + 38 + 48 + 43 + 83 + 84 + 348 + 384 + 834 + 843 + 438 + 483  = 3675

If the number has a digit 0, the numbers formed by a leading 0 should be discarded:

sc_perm_comb(340) = 3 + 4 + 34 + 30 + 40 + 43 + 340 + 304 + 430 + 403 = 1631

Duplicate permutations can occur if the number has more than once the same digit, but they should be added only once in the result:

sc_perm_comb(333) = 3 + 33 + 333 = 369

If the number has only one digit its score is the same number:

sc_perm_comb(6) = 6
sc_perm_comb(0) = 0


Started: Mar 20th, 2025 @ :10:05am ET
Intervals: 1
Ended: Mar 20th, 2025 @ 10:35am ET
"""