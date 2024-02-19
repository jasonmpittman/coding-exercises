__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Bulls and Cows:

Create a four digit random number from the digits 1 to 9, without duplication.

The program should:

1. ask for guesses to this number
2. reject guesses that are malformed
3. print the score for the guess

The score is computed as:

A. The player wins if the guess is the same as the randomly chosen number, and the program ends.

B. A score of one bull is accumulated for each digit in the guess that equals the corresponding digit in the randomly chosen initial number.

C. A score of one cow is accumulated for each digit in the guess that also appears in the randomly chosen number, but in the wrong position.

Started: Feb 19, 2024 @ 5:10am ET
Intervals: 1
Ended: Feb 19, 2024 @ 5:33am ET
"""
import random

def get_random_number() -> int:
    random_number = ''

    for i in range (1,5):
        random_number += str(random.randint(1, 9))

    return random_number

def get_player_guess() -> int:
    guess = input("Enter a four digit number: ")

    return guess
    
# I think this works correctly based on limited testing
def score_guess(n, guess):
    bull, cow = 0, 0

    for c in guess:
        if c in n and guess.index(c) == n.index(c):
            bull += 1
        elif c in n:
            cow += 1
        
    return bull, cow

if __name__ == "__main__":
    number = get_random_number()
    print(number)
    bulls, cows = 0, 0

    while True:
        guess = get_player_guess()

        if guess == number:
            print("You guessed correctly!")
            break
        else:
            b, c = score_guess(number, guess)
            bulls += b
            cows += c
            print("Bulls: {} Cows: {}".format(bulls, cows))
    