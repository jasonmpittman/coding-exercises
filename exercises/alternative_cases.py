__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2024"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

"""
Create a function that alternates the case of the letters in a string (known as Spongecase).
Examples

    alternating_caps("Hello") ➞ "HeLlO"

    alternating_caps("How are you?") ➞ "HoW aRe YoU?"

    alternating_caps("OMG this website is awesome!") ➞ "OmG tHiS wEbSiTe Is AwEsOmE!"

Started: Feb 04, 2025 @ 7:40am 
Intervals: 1
Ended: Feb 04, 2025 @ 8:03am 
"""

def alternate_caps(string_input):
    # get length of string
    string_length = len(string_input)
    string_list = list(string_input)

    # loop over the odd indices and convert c to upper
    for i in range(0, string_length, 2):
        string_list[i] = string_input[i].upper()

    print("".join(string_list))

if __name__ == '__main__':
    string_input = input("Enter as string to convert: ")

    alternate_caps(string_input.lower())


