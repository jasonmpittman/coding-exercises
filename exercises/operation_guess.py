__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Operation Guess:
You have a string of numbers; starting with the third number each number is the result of an operation performed using the previous two numbers.

Complete the function which returns a string of the operations in order and separated by a comma and a space, e.g. "subtraction, subtraction, addition"

The available operations are (in this order of preference):

1) addition
2) subtraction
3) multiplication
4) division

Notes:

    All input data is valid
    The number of numbers in the input string >= 3
    For a case like "2 2 4" - when multiple variants are possible - choose the first possible operation from the list (in this case "addition")
    Integer division should be used

Example
    "9 4 5 20 25"  -->  "subtraction, multiplication, addition"

    Because:
    9 - 4 = 5   --> subtraction
    4 * 5 = 20  --> multiplication
    5 + 20 = 25 --> addition

Started: Feb 15, 2025 @ 4:10am ET
Intervals: 1
Ended: Feb 15, 2025 @ 4:27am ET
"""

def guess_operation(numbers: str) -> str:
    list_of_numbers = numbers.split(' ')
    operations = []
    number_of_numbers = len(list_of_numbers)

    for i in range(number_of_numbers - 2):
        if int(list_of_numbers[i]) + int(list_of_numbers[i + 1]) == int(list_of_numbers[i + 2]):
            operations.append('addition, ')
            
        elif int(list_of_numbers[i]) - int(list_of_numbers[i + 1]) == int(list_of_numbers[i + 2]):
            operations.append('subtraction, ')
            
        else:
            operations.append('multiplication, ')


    return ''.join(operations)


if __name__ == "__main__":
    numbers = "9 4 5 20 25"
    operations = guess_operation(numbers)

    print(operations)