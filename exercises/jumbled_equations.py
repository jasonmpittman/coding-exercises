__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
In this challenge, you are given a list of one or more arithmetic operators and a list of numbers. Take each of the operators and mate it with any three separate numbers in the list to create a valid equation. Your answer should contain all possible equations.

Examples

    jumbled([["+"], [2, 1, 3]]) ➞ ["1+2=3"]
    jumbled(["+", "*"], [36, 28, 71, 4, 12, 7, 11]]) ➞ ["4*7=28", "4+7=11"]
    jumbled([["+", "-", "*", "**"], [1, 2, 3, 0]]) ➞ ["1+2=3", "2**0=1", "3**0=1", "3-1=2", "3-2=1"]
    # Each equation must contain 3 discrete numbers from the list.
    # "1+0=1" or "3-3=0" are not allowed.

Start: 05:15am
End: 05:36:am
Cycles: 1
"""
import operator
import random

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def unjumbled_equation(operators: list, values: list):
    equations = []
    values.sort()

    for operator in operators:
        selected_values = random.sample(values, 2)
        result = operations[operator](selected_values[0], selected_values[1])
        print(f'{selected_values[0]} {operator} {selected_values[1]} = {result}')

    return equations

if __name__ == "__main__":
    equation_parts = [["+", "*"], [36, 28, 71, 4, 12, 7, 11]] #[["+"], [2, 1, 3]]
    operators = equation_parts[0] 
    values = equation_parts[1]

    unjumbled_equation(operators, values)

