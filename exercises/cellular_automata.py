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

Part Three: develop neighborhood function 
Started: Feb 21th, 2025 @ 7:45am ET
Intervals: 1
Ended: Feb 21th, 2025 @ 8:15am ET

Part Four: develop neighborhood function 
Started: Feb 22th, 2025 @ 7:25am ET
Intervals: 1
Ended: Feb 22th, 2025 @ 7:55am ET
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
    if pattern.index(cell) != 0 or pattern.index(cell) != len(pattern):
        return "".join([str(pattern[cell - 1]), str(cell), str(pattern[cell + 1])])

def update_cell_state(neighborhood: str, rule_set: list) -> int:
    updated_state = rule_set[neighborhood] 

    return updated_state

# TODO: verify rule is applied correctly in update cell state function
def run_ca(starting_pattern: list, rule_set: dict, time: int):
    pattern = starting_pattern
    i = 1
    
    while i <= time:
        print("Generation {}: {}".format(i, pattern))
        
        for cell in pattern:
            index = pattern.index(cell)
            #print("Index of current cell: ", index)
            neighborhood = get_neighborhood(pattern, cell)
            #print("Current neighborhood: ", neighborhood)
            updated_cell = update_cell_state(neighborhood, rule_set)
            #print("Updated cell value: ", updated_cell)
            pattern[index] = int(updated_cell)

        i += 1

if __name__ == "__main__":
    rule = sys.argv[1]
    starting_pattern = [0,1,0,0,1,0,1,0]
    time = 10

    converted_rule = convert_rule(int(rule))
    rule_set = build_rule_set(converted_rule)

    #print(rule_set)

    run_ca(starting_pattern, rule_set, time)    