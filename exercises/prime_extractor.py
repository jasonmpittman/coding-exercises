__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Prime Extractor:
Create a function that takes an integer argument and returns an array of prime numbers found in the decimal representation of that number (not factors).

For example, extractPrimes(1717) returns [7, 7, 17, 17, 71].

The array should be in ascending order. If a prime number appears more than once, every occurrence should be listed. If no prime numbers are found, return an empty array.

Examples
    extractPrimes(1) ➞ []
    extractPrimes(7) ➞ [7]
    extractPrimes(73) ➞ [3, 7, 73]
    extractPrimes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]

Started: April 08, 2024 @ 7:25am ET
Intervals: 1
Ended: April 08, 2024 @ 7:41am ET
"""
from sys import argv

# test any integer for primality
def is_prime(n: int) -> bool:
    if n > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (n//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

# generate list of substrings from given string
def get_substrings(string: str) -> list:
    substrings = []

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substrings.append(string[i:j])

    return substrings

def extract_primes(string: str) -> list:
    primes = []

    # get substrings of string
    substrings = get_substrings(string)

    # test substrings for primality
    for s in substrings:
        if is_prime(int(s)):
            primes.append(int(s))

    return primes


if __name__ == "__main__":
    string = argv[1]

    primes = extract_primes(string)
    print(sorted(primes))