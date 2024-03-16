__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Drink Sort:
You will be given an array of drinks, with each drink being an object with two properties: name and price. Create a function that has the drinks array as an argument and return the drinks objects sorted by price in ascending order.

Started: Mar 16, 2024 @ 5:40am ET
Intervals: 1
Ended: March 16, 2024 @ 6:00am ET
"""
import json

def sort_drinks(data: dict) -> dict:
    print(data)

    data['drinks'] = list(sorted(data['drinks'], key=lambda d: d['price']))

    print(data)

if __name__ == "__main__":
    with open("drinks.json") as f: # FileNotFoundError is not run from /exercises
        data = json.load(f)
    
    sort_drinks(data)