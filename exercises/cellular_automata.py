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

    print(rule_set)

def update_cell_state(current_state: int, neighborhood: str, rule: str) -> int:
    updated_stated = 0

    converted_rule = convert_rule(int(rule))

    build_rule_set(converted_rule)

    return updated_stated

if __name__ == "__main__":
    rule = sys.argv[1]

    update_cell_state(1, '101', rule)