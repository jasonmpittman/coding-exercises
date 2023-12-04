#!/usr/bin/env python

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"



""" Propositional Evaluator

Write a function that evaluates a simple propositional logic expression. The expression will be given as a string containing variables (A, B, C, etc.), logical operators (AND, OR, NOT), and parentheses for grouping. Your function should be able to evaluate the truth value of the expression given a set of truth values for each variable.

    evaluateLogic("A AND B", {"A": True, "B": False}) should return False.
    evaluateLogic("NOT (A OR B)", {"A": False, "B": False}) should return True.
    evaluateLogic("(A OR B) AND (C OR NOT A)", {"A": True, "B": True, "C": False}) should return True.

    A=True;B=False
    A AND B
    
Started: Dec 04, 2023 @ 5:45am ET
Intervals: 1
Ended: Dec 04, 2023 @ 6:15am ET 

"""

def get_propositions():
    variables = input('Enter expression as p=value;q=value: ')
    propositions = dict(x.split('=') for x in variables.split(';'))
    
    return propositions

def get_statement():
    statement = input('Enter the statement: ')
    
    return statement

# TODO: add negation operator and parentheses
def evaluate_satement(statement, propositions):
    connective = parse_connective(statement)

    if connective == 'AND':
        if propositions['A'] == 'True' and propositions['B'] == 'True':
            return True
        else:
            return False

    if connective == 'OR':
        if propositions['A'] == 'True' or propositions['B'] == 'True':
            return True
        else:
            return False 


def parse_connective(statement):
    # A AND B
    # NOT (A OR B)

    if 'AND' in statement:
        return 'AND'
    elif 'OR' in statement:
        return 'OR'

if __name__ == '__main__':
    propositions = get_propositions()
    statement = get_statement()

    value = evaluate_satement(statement, propositions)
    print(value)


    