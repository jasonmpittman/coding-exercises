__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Cellular Automata:

Part One: develop rule generator
Started: Feb 19th, 2025 @ 02:00am ET
Intervals: 1
Ended: Feb 19th, 2025 @ 2:30am ET

Part Two: develop neighborhood function 
Started: Feb 20th, 2025 @ 6:50am ET
Intervals: 1
Ended: Feb 20th, 2025 @ 7:20am ET
"""
import sys


def convert_rule(rule: int) -> str:
    return format(rule, '08b') 

def build_rule_set(converted_rule: str):
    base = [
        '000',
        '001',
        '010',
        '011',
        '100',
        '101',
        '110',
        '111'
    ]

    rule_set = {}
    i = 0

    for b in base:
        rule_set[b] = converted_rule[i]
        i += 1

    return rule_set

def get_neighborhood(pattern: list, cell: int) -> list:
    if pattern[cell] != pattern[0] or pattern[cell] != pattern[len(pattern)]:
        return [pattern[cell - 1], pattern[cell + 1]]

def update_cell_state(current_state: int, neighborhood: str, rule: str) -> int:
    updated_stated = 0



    return updated_stated

def run_ca(starting_pattern: list, rule_set: dict, time: int):
    pattern = starting_pattern
    i = 1

    while time >= 0:
       pass
       
       
       #update_cell_state(1, '101', rule) 


if __name__ == "__main__":
    rule = sys.argv[1]
    starting_pattern = [0,1,0,0,1,0,1,0]

    converted_rule = convert_rule(int(rule))
    rule_set = build_rule_set(converted_rule)

    