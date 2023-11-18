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
