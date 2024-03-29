__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Moon Sum:
When two numbers are added together, the strange Lunar arithmetic is used on the Moon. The Lunar sum of two numbers is not determined by the sum of their individual digits, but by the highest digit of the two taken into account at each step, in columnar form.

2  4  6  +
3  1  7  =
--------
3  4  7

// 3 > 2 | 4 > 1 | 7 > 6

1  3  4  +
   5  4  =
--------
1  5  4

//  1 > 0 | 5 > 3 | 4 == 4
// Blank spots in the columnar form are equals to 0

   2  0  +
1  4  0  =
-------
1  4  0

// 1 > 0 | 4 > 2 | 0 == 0

Started: Mar 14, 2024 @ 5:30am ET
Intervals: 1
Ended: March 14, 2024 @ 5:45am ET
"""
from sys import argv


def add(n: list, m: list, mode=None) -> int:
   total = ""

   if mode is None:
      for i in range(len(n)):
         if int(n[i]) > int(m[i]):
            total += n[i]
         else:
            total += m[i]

   if mode == "comp":
      total = ''.join([n[i] if int(n[i]) > int(m[i]) else m[i] for i in range(len(n))])


   return total


if __name__ == "__main__":
   n = argv[1].split(',')
   m = argv[2].split(',')

   total = add(n, m) # 2,4,6 3,1,7
   print(total)

   total = add(n, m, mode="comp")
   print(total)