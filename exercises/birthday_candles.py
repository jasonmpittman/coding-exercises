__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Birthday Candles:
Given a string containing digits (representing the strength of the candles), calculate the number of blows you need to extinguish all the candles.

Starting at the beginning of the string, each blow can only reach 3 candles, reducing their strength by one each. You can only reach more candles once those directly in front of you are extinguished.

Examples
    Input: "1321"
    Move 1 | "(132)1" -> "0211"
    Move 2 | "0(211)" -> "0100"
    Move 3 | "0(100)" -> "0000"

    This should return 3.

    Input: "0323456"
    Move 1 | "0(323)456" -> "0212456"
    Move 2 | "0(212)456" -> "0101456"
    Move 3 | "0(101)456" -> "0000456"   
    Move 4 | "0000(456)" -> "0000345"
    Move 5 | "0000(345)" -> "0000234"
    Move 6 | "0000(234)" -> "0000123"
    Move 7 | "0000(123)" -> "0000012"
    Move 8 | "00000(12)" -> "0000001"
    Move 9 | "000000(1)" -> "0000000"

    This should return 9.

    Input: "2113"
    Move 1 | "(211)3" -> "1003"
    Move 2 | "(100)3" -> "0003"
    Move 3 | "000(3)" -> "0002"
    Move 4 | "000(2)" -> "0001"
    Move 5 | "000(1)" -> "0000"

    This should return 5.


Started: May 15, 2024 @ 11:55am ET
Intervals: 1
Ended: May 15, 2024 @ 12:15pm
"""
from sys import argv

# TODO: implement pseudocode algorithm
def blow_candles(candles: list) -> str:
    candles_string = ''
    breath = 3 # this is how many candles we can affect each blow
    number_of_candles = len(candles)

    # for candle in candles
    # if candle not 0
    # while candles[0] is > 0
    # -1 to candles 0,1,2 (don't allow negative)
    #


if __name__ == "__main__":
    candles = list(map(int, argv[1].split(',')))
