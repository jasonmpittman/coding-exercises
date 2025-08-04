__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"
__difficuluty__ = ""

"""
ccwc - a 'wc' clone

part 1: clone -c argument (19 minutes)
part 2: clone -l argument
part 3: clone -w argument
part 4: clone -m argument
part 5: clone default as -clw
part 6: clone read from stdout as input

Start: 7.29.25 3:00am, 8.01.25 5:45am, 8.02.25 5:42am, 8.04.25 6:25am
End:
Cycles: 3
"""
import os
import re
import argparse

#   -c The number of bytes in each input file is written to the standard output.  This will cancel out any prior usage of the -m option.
def get_file_bytes(file: str) -> int:
    number_of_bytes = 0

    try:
        number_of_bytes = os.path.getsize(file)
    except Exception as e:
        print(f'An error occured while attempting to get bytes in file: {e}')

    return number_of_bytes

def get_number_of_lines(file: str) -> int:
    """ Returns the number of lines in each input file is written to the standard output. """
    number_of_lines = 0

    try:
        with open(file, 'r') as f:
            number_of_lines = len(f.readlines())
    except Exception as e:
        print(f'An error occured while attempting to access the file: {e}')

    return number_of_lines

#   TODO: undercounting because of pattern match filter
def get_number_of_words(file: str) -> int:
    number_of_words = 0
    clean_words = []
    pattern = r"\b\w+\b"

    try:
        with open(file, 'r') as f:
            lines = f.readlines()

            for line in lines:
                words = line.split(' ')
                for word in words:
                    if re.match(pattern, word):
                        clean_words.append(word)

            number_of_words = number_of_words + len(clean_words)
    except Exception as e:
        print(f'An error occured whlie attempting to access the file: {e}')

    return number_of_words

def get_number_of_characters(file: str) -> int:
    """ The number of characters in each input file is written to the standard output. """
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A Python clone of the wc utility')
    parser.add_argument('-c', help='The number of bytes in each input file')
    parser.add_argument('-l', help='The number of lines in each input file')
    parser.add_argument('-w', help='The number of words in each input file')
    parser.add_argument('-m', help='The number of characters in each input file')

    args = vars(parser.parse_args())

    if args['c']:
        result = get_file_bytes(args['c'])
        print('    ' + str(result) + ' ' + args['c'])
    
    if args['l']:
        result = get_number_of_lines(args['l'])
        print('    ' + str(result) + ' ' + args['l'])
    
    if args['w']:
        result = get_number_of_words(args['w'])
        print('    ' + str(result) + ' ' + args['w'])
    
    if args['m']:
        result = get_number_of_characters(args['m'])
        print('    ' + str(result) + ' ' + args['w'])
