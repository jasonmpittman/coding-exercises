__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Consecutive Ascending:
Write a function that will return true if a given string (divided and grouped into a size) will contain a set of consecutive ascending numbers, otherwise, return false.

Examples:
    ascending("123124125") ➞ true
    // Contains a set of consecutive ascending numbers
    // if grouped into 3's : 123, 124, 125

    ascending("101112131415") ➞ true
    // Contains a set of consecutive ascending numbers
    // if grouped into 2's : 10, 11, 12, 13, 14, 15

    ascending("32332432536") ➞ false
    // Regardless of the grouping size, the numbers can't be consecutive.

    ascending("326325324323") ➞ false
    // Though the numbers (if grouped into 3's) are consecutive but descending.

    ascending("666667") ➞ true
    // Consecutive numbers: 666 and 667.

Started: June 04, 2024 @ 4:30am ET
Intervals: 1
Ended: June 04, 2024 @ 5:00am ET
"""