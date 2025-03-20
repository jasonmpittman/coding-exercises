__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Reach and Sum:
Make a function that receives three arguments in this order:

    init_val (initVal) is the starting number;
    pattern_l (patternL) is the list of repeating differences;
    nth_term (nthTerm) is the ordinal position of the term in the sequence (≤ 1,500,000).

The function should return the sum of the digits of the nth_term in the sequence.
Example Cases:

sum_dig_nth_term(10, [2, 1, 3], 6) → 10  
# 6th term = 19 → sum of digits = 1 + 9 = 10  

sum_dig_nth_term(10, [1, 2, 3], 15) → 10  
# 15th term = 37 → sum of digits = 3 + 7 = 10  


Started: Mar 11th, 2025 @ 6:10am ET
Intervals: 1
Ended: Mar 11th, 2025 @ 6:40am ET
"""
import sys

# TODO: the generator does the 4th term incorrectly. should be 18 and its 20. the first run is correct 10, 12, 13, 16
def generate_list_of_terms(init_val: int, pattern: list, nth_term: int) -> list:
    terms = [0,0,0,0]
    term_1, term_2, term_3, term_4 = 0,0,0,0
    i = 1

    while i <= nth_term:
       term_1 = term_1 + init_val
       print(term_1)

       term_2 = term_2 + term_1 + int(pattern[0])
       print(term_2)

       term_3 = term_3 + term_2 + int(pattern[1])
       print(term_3)
       
       term_4 = term_4 + term_3 + int(pattern[2])
       print(term_4)

       # do this better by .insert() and use terms[n] instead of variables 
       terms.clear()
       terms.append(term_1)
       terms.append(term_2)
       terms.append(term_3)
       terms.append(term_4)

       i += 1
       
    return terms

def sum_terms(terms: list) -> int:
    summed_term = 0


    return summed_term


if __name__ == "__main__":
    init_val = int(sys.argv[1])
    pattern = sys.argv[2].split(',')
    nth_term = int(sys.argv[3])
    
    print(init_val, pattern, nth_term)

    terms = generate_list_of_terms(init_val, pattern, nth_term)
    print(terms)