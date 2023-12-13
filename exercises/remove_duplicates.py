
__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"


""" Remove Duplicates: https://www.seminolestate.edu/computers/competition/samples/2005

Create an application that removes duplicate entries from a list of numbers. Your application will process a maximum of 20 integer numbers. Each number will be equal to or greater than zero. You do not need to edit for floating point numbers or invalid characters. Twenty is the maximum number of values to be entered. The user must be able to enter 0 numbers, 1 number, 20 numbers or any amount between 1 and 20. If you create a command-line application, allow the user to enter -1 to indicate that no more numbers will be entered. Once the input is complete, the application must indicate which numbers are duplicated and how many duplicates existed for each number.

Print the original list of numbers entered. Next, print a list of any numbers that were duplicated and the number of duplicates. Finally, print the revised list of numbers minus any duplicates.

Sample:
    Input: 1 2 3 4 5 1 6 1 7 1 8 1 9 1 10 -1
    Output: Value 1: 5 copies are deleted
                     1 2 3 4 5 6 7 8 9 10

    Input: 1 2 1 2 1 2 1 2 3 4 5 3 -1
    Output: Value 1: 3 copies are deleted
            Value 2: 3 copies are deleted
            Value 3: 1 copies are deleted
                     1 2 3 4 5

Started: Dec 13, 2023 @ 5:30am ET
Intervals: 1.25
Ended: Dec 13, 2023 @ 6:15am ET

"""

def remove_duplicates(numbers: list) -> set | dict:
    cleaned_numbers = set()
    duplicates = {}
    count = 0

    for n in numbers:
        if n in cleaned_numbers:
            # increment count for n key in dict
            duplicates[n] += 1
        else:
            duplicates[n] = 1 # add n as key in dict
            cleaned_numbers.add(n)

    return cleaned_numbers, duplicates

if __name__ == '__main__':
    number = 0
    numbers = []

    while number != -1:
        number = int(input('Enter a number between 0 and 20: '))
        if number != -1:
            numbers.append(number)

    print(numbers)

    cleaned_numbers, duplicates = remove_duplicates(numbers)

    for k,v in duplicates.items():
        if v > 1:
            print(f'Value {k}: {v} copies are deleted')

    print(cleaned_numbers)