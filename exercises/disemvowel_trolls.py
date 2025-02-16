
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Disemvowel Trolls:
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Started: Feb 16, 2025 @ 7:15pm ET
Intervals: 1
Ended: Feb 16, 2025 @ 7:23am ET
"""

def disemvowel_string(string: str) -> str:
    vowels = ["a", "i", "e", "o", "u"]

    for vowel in vowels:
        string = string.replace(vowel, "")
    
    print(string)


if __name__ == "__main__":
    string = "This website is for losers LOL!"
    disemvowel_string(string)