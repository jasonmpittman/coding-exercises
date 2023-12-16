__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Test Fibonacci

Write unit tests for a function named fibonacci which takes a non-negative integer n as input and returns the n-th Fibonacci number. Your goal is to thoroughly test the function covering various scenarios and edge cases.\

    Base Cases: Test for the base cases, like 0, 1.
    Positive Integers: Test with a variety of positive integers.
    Large Numbers: Test the function with a large value of n to check its performance.
    Invalid Inputs: Test how the function handles invalid inputs like negative numbers, non-integer values, or extremely large values that could cause performance issues.
    Edge Cases: Include edge cases that you think could challenge the boundaries of the function.

Started: Dec 16, 2023 @ 5:10am ET
Intervals: 1
Ended: Dec 16, 2023 @ 5:40am ET   
"""
import time
import unittest

try:
    from exercises import fibonacci
except ImportError as e:
    print(e)


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self._started_at = time.time()

    def test_base_case(self):
        self.assertEqual(fibonacci.fibonacci(0), 0)

    def test_not_base(self):
        self.assertNotEqual(fibonacci.fibonacci(0), 1)

    def test_positive_integers(self):
        self.assertTrue(fibonacci.fibonacci(1), 1)
        self.assertTrue(fibonacci.fibonacci(2), 1)
    
    def test_not_positive(self):
        self.assertIsNot(fibonacci.fibonacci(1), 2)

    def test_large_number(self):
        self.assertEqual(fibonacci.fibonacci(1234), 347746739180370201052517440604335969788684934927843710657352239304121649686845967975636459392453053377493026875020744760145842401792378749321113719919618588095724485583919541019961884523908359133457357334538791778480910430756107407761555218113998374287548487)

    def test_negative_number(self):
        self.assertEqual(fibonacci.fibonacci(-1), 0)

    def test_invalid_char(self):
        with self.assertRaises(TypeError):
             fibonacci.fibonacci('a')

    def tearDown(self) -> None:
        elapsed_time = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed_time, 2)))


if __name__ == '__main__':
    unittest.main()
