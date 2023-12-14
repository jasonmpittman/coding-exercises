__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Test Reverse String:

Write unit tests for a function named reverse_string which takes a string as input and returns its reverse. Your goal is to cover various scenarios and edge cases to ensure the function behaves as expected.

Consider these scenarios:

    Normal Case: Test with a regular string like "hello".
    Empty String: Test to ensure an empty string returns an empty string.
    Single Character: Test with a single character, like "a".
    Palindrome: Test with a palindrome, like "radar".
    Special Characters: Include special characters, numbers, and spaces in the test.
    Unicode Characters: Test with Unicode characters to ensure it handles different character sets.
    Long String: Test with a very long string to see if there are any performance issues.

Started: Dec 13, 2023 @ 5:45am ET
Intervals: 1.25
Ended: Dec 13, 2023 @ 6:15am ET

"""
import unittest

try:
    from exercises import reverse_string 
except ImportError as e:
    print(e)

class ReverseStringTest(unittest.TestCase):
    def test_reverse_normal(self):
        self.assertEqual(reverse_string.reverse_string('hello'), 'olleh', 'The reversed string is incorrect')

    def test_reverse_empty(self):
        self.assertRaises(TypeError, reverse_string.reverse_string(' '))

    def test_reverse_single_char(self):
        self.assertEqual(reverse_string.reverse_string('a'), 'a', 'The reversed string is incorrect')

    def test_reverse_palindrome(self):
        self.assertEqual(reverse_string.reverse_string('radar'), 'radar', 'The reversed string is incorrect')

    def test_reverse_special_chars(self):
        reversed = reverse_string.reverse_string('t3$t')
        self.assertIsNot(reversed, 't$3t', 'The reversed string with special characters is correct')

    #def test_reverse_unicode_chars(self):
    #    self.assertEqual()

    #def test_reverse_long(self):
    #    self.assertEqual()


if __name__ == '__main__':
    unittest.main()