__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
This challenge involves a series that can start with any string of digits. The next term in the series is found by adding the digits of the previous term, appending that sum to the previous term, and then truncating the leftmost digits so that the number of digits in the terms is always the same.

Let's start with "1234". The sum of the digits is 10. Appending gives us "123410", then truncating the left two digits results in "3410". The next three terms are "4108", "0813", "1312". The series becomes periodic when a term that previously appeared occurs again.

Example:

"124", "247", "713", "311", "115", "157", "713", "311" ...

This series becomes periodic at a length of 6 before "713" reappears.

Create a function whose argument is a digit string (the first term) and returns the length of the series when it first becomes periodic.

Examples
    periodic("1") ➞ 1
    periodic("3061") ➞ 7
    periodic("02468") ➞ 178
    periodic("314159265") ➞ 12210

Start: 05:25am
End: 05:45:am
Cycles: 1
"""
from sys import argv

def sum_digits(term):
    sum_of_digits = 0

    for digit in term:
        sum_of_digits += int(digit)
    
    return sum_of_digits

def periodic(first_term: str, series=None) -> int:
    series_length = 0
    series = []
    is_periodic = False

    while is_periodic == False:
        #   sum of digits in first term
        term_sum = sum_digits(first_term)
        
        print(f'sum of digits in first term is {term_sum}')

        #   append sum to first term then
        appended_term = first_term + str(term_sum)
        print(f'Appended term is {appended_term}')

        #   truncate left digit(s) to keep term the same length to get next term
        truncate_length = len(appended_term) - len(first_term)
        truncated_term = appended_term[truncate_length::]
        print(f'Truncated term is {truncated_term}')

        #   if new term in set of terms, length of set has become periodic
        if truncated_term in series:
            series_length = len(series) + 1 #   need to add 1 bc we don't add the first term to the list
            is_periodic = True
        else:
            series.append(truncated_term)
            first_term = truncated_term #   little hack to make the loop work?

    return series_length

if __name__ == "__main__":
    first_term = argv[1]

    result = periodic(first_term)
    print(result)



