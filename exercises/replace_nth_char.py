__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
Create a function that takes a string and replaces every nth instance of old_char with new_char. Your function will have four parameters:

    txt — The original input text to be processed.
    nth — The nth instance to be replaced.
    old_char — The character being replaced.
    new_char — The character replacing old_char.

In other words, if txt is "abababa", nth is 3, old_char is "a" and new_char is "Z", you would replace the 3rd insrtance of "a" with "Z", returning "ababZba".
Examples

replace_nth("A glittering gem is not enough.", 0, "o", "-")
➞ "A glittering gem is not enough."

replace_nth("Vader said: No, I am your father!", 2, "a", "o")
➞ "Vader soid: No, I am your fother!"

replace_nth("Writing a list of random sentences is harder than I initially thought it would be.", 2, "i", "3")
➞ "Writ3ng a list of random sentences 3s harder than I in3tially thought 3t would be."

Start: 5:35am
End: 6:05:am
Cycles: 1
"""