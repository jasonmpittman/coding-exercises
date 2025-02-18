__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Remove Odd Hashes:

remove any hash whose two keys sum to an odd number.

example:

remove_odd_hashes(
  [ {a: 5, b: 5}, 
    {a: 3, b: 4}, 
    {a: 2, b: 0}, 
    {a: 2, b: 1}], 
  :a, :b)
  
# returns [{a: 5, b: 5}, {a: 2, b: 0}]


Started: Feb 18th, 2025 @ 12:55pm ET
Intervals: 1
Ended: Feb 18th, 2025 @ 1:17pm ET
"""

def remove_odd_hashes(hashes: list) -> list:
    a = 0
    b = 1
    even_hashes = []
    
    for hash in hashes:
        if (hash['a'] + hash['b']) % 2 == 0:
            even_hashes.append(hash)
            #even_hashes.append(hash)
        #for key, value in hash.items():
            #print(key[a], key[b])
            #if (item['a'] + item['b']) % 2 == 0:
            #    even_hashes.append({item[a], item[b]})
            #a += 1
            #b += 1

    return even_hashes

if __name__ == "__main__":
    hashes = [
        {'a': 5, 'b': 5},
        {'a': 3, 'b': 4},
        {'a': 2, 'b': 0},
        {'a': 2, 'b': 1}
    ]

    even_hashes = remove_odd_hashes(hashes)
    print(even_hashes)