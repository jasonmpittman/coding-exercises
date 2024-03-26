__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Polybius Square:
The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).

To encipher a message, each letter is merely replaced by its row and column numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.

Examples:
    polybius("Hi") ➞ "2324"
    polybius("2324  4423154215") ➞ "hi there"
    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

Started: Mar 26, 2024 @ 4:45am ET
Intervals: 1
Ended: March 26, 2024 @ 5:15am ET
"""