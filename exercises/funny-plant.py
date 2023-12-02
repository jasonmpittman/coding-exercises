#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""Funny Plant: https://old.reddit.com/r/dailyprogrammer/comments/3twuwf/20151123_challenge_242_easy_funny_plant/

Scientist have discovered a new plant. The fruit of the plant can feed 1 person for a whole week and best of all, the plant never dies. Fruits needs 1 week to grow, so each weak you can harvest it fruits. Also the plant gives 1 fruit more than the week before and to get more plants you need to plant a fruit.

Now you need to calculate after how many weeks, you can support a group of x people, given y fruits to start with.

Input
    15 1

Output
    5

Input description:
The input gives you 2 positive integers x and y, being x the number of people needed to be fed and y the number of fruits you start with.

Output description

The number of weeks before you can feed the entire group of people.
    
    Input
    200 15
    50000 1
    150000 250

    Output
    5
    14
    9 

Started: Dec 02, 2023 @ 7:00am ET
Intervals: 1
Ended: Dec 02, 2023 @ 7:30am ET 
"""

def get_input():
    number_of_people = int(input("Give the number of people: "))
    number_of_starting_fruits = int(input("Give the number of starting fruits: "))

    return number_of_people, number_of_starting_fruits

# TODO: Derive the number of weeks before you can feed the entire group of people.
def grow_fuit(number_of_starting_fruits, number_of_people):
    weeks_to_feed_all = 1
    total_fruits = 0

    # the problem can be solved through a fibnonacci application
    while total_fruits <= number_of_people:
        total_fruits = total_fruits + number_of_starting_fruits
        number_of_starting_fruits = total_fruits + number_of_starting_fruits
        weeks_to_feed_all += 1
        

    return weeks_to_feed_all




if __name__ == '__main__':
    number_of_people, number_of_starting_fruits = get_input()
    
    weeks_to_feed_all = grow_fuit(number_of_starting_fruits, number_of_people)
    print(weeks_to_feed_all)
    
    
