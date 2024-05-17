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
         May 16, 2024 @ 5:50am ET
Intervals: 2
Ended: May 15, 2024 @ 12:15pm
Ended: May 16, 2024 @ 6:20am
"""
from sys import argv

# TODO: working but not correct output
def blow_candles(candles: str) -> int:
    blows = 0
    
    while '1' in candles or '2' in candles or '3' in candles:
        i = 0
        while i < len(candles):
            if candles[i] != '0':
                j = min(i + 3, len(candles))
                candles = candles[:i] + ''.join(['0' for _ in range(i, j)]) + candles[j:]
                blows += 1
            else:
                i += 1
    
    return blows

if __name__ == "__main__":
    candles = argv[1] # 1321 # 2113 # 0323456
    
    blows = blow_candles(candles)
    print(blows)
