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

part 1: clone -c argument
part 2: clone -l argument
part 3: clone -w argument
part 4: clone -m argument
part 5: clone default as -clw
part 6: clone read from stdout as input

Start: 7.29.25 3:00am
End:
Cycles: 1
"""
import os
import argparse

#   -c The number of bytes in each input file is written to the standard output.  This will cancel out any prior usage of the -m option.
def get_file_bytes(file: str) -> int:
    number_of_bytes = 0

    try:
        number_of_bytes = os.path.getsize(file)
    except Exception as e:
        print(f'An error occured while attempting to get bytes in file: {e}')

    return number_of_bytes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A Python clone of the wc utility')
    parser.add_argument('-c', help='The number of bytes in each input file')

    args = vars(parser.parse_args())

    if args['c']:
        result = get_file_bytes(args['c'])
        print('    ' + str(result) + ' ' + args['c'])