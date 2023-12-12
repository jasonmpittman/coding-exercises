__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

import unittest

try:
    from exercises import hello_world 
except ImportError as e:
    print(e)

class HellowWorldTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world.hello(), "Hello, World!")
    
    def test_hello_negative(self):
        self.assertEqual(hello_world.hello(), "Hello World!")
