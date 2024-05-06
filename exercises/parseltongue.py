__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Parseltongue:
Hermione has come up with a precise formula for determining whether or not a phrase was ssspoken by a parssseltongue (a reference from the Harry Potter universe; the language of ssserpents and those who can converse with them).

Each word in a sssentence must contain either:

    Two or more consecutive instances of the letter "s" (i.e. must be together ss..), or...
    Zero instances of the letter "s" by itself.

Examples
    isParselTongue("Sshe ssselects to eat that apple. ") ➞ true
    isParselTongue("She ssselects to eat that apple. ") ➞ false
    // "She" only contains one "s".
    isParselTongue("Beatrice samples lemonade") ➞ false
    // While "samples" has 2 instances of "s", they are not together.
    isParselTongue("You ssseldom sssspeak sso boldly, ssso messmerizingly.")

Started: May 06, 2024 @ 6:15am ET
Intervals: 1
Ended: May 06, 2024 @ 6:45am ET
"""