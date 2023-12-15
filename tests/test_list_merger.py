__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Test List Merger

Consider these scenarios:

    Normal Case: Both lists contain elements in sorted order.
    Empty Lists: Both lists are empty.
    One Empty List: One list is empty, and the other is not.
    Single Element Lists: Each list contains only one element.
    Duplicate Elements: Lists contain some duplicate elements.
    Negative Numbers: Lists contain negative numbers.
    Large Numbers: Lists contain very large numbers.
    Non-Integer Elements: (Optional) If your function should handle this, include lists with strings or other types.

Started: Dec 15, 2023 @ 5:10am ET
Intervals: 1
Ended: Dec 15, 2023 @ 5:40am ET   
"""

import time
import random
import unittest

try:
    from exercises import list_merger
except ImportError as e:
    print(e)

class TestListMerger(unittest.TestCase):
    
    def setUp(self):
        self._started_at = time.time()
        self.list_a = [1, 3, 5]
        self.list_b = [2, 4, 6]
        self.list_empty = []
        self.list_a_large = sorted([random.randint(0, 10000) for _ in range(100000)])
        self.list_b_large = sorted([random.randint(0, 10000) for _ in range(100000)])

    def tearDown(self) -> None:
        elapsed_time = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed_time, 2)))
        
    def test_normal_case(self):
        self.assertEqual(list_merger.merge_sorted_lists(self.list_a, self.list_b), [1,2,3,4,5,6])
    
    def test_empty_case(self):
        self.assertEqual(list_merger.merge_sorted_lists(self.list_empty,self.list_empty), self.list_empty)
    
    def test_one_empty_case(self):
        self.assertEqual(list_merger.merge_sorted_lists(self.list_a, self.list_empty), [1,3,5])
        self.assertEqual(list_merger.merge_sorted_lists(self.list_empty, self.list_a), [1,3,5])
    
    def test_single_case(self):
        self.assertEqual(list_merger.merge_sorted_lists([1], [2]), [1,2])
        self.assertNotEqual(list_merger.merge_sorted_lists([1], [2]), [2,1])

    # bonus
    def test_large_lists(self):
        self.assertEqual(list_merger.merge_sorted_lists(self.list_a_large, self.list_b_large), self.list_a_large + self.list_b_large, 'The lists are no equal')


if __name__ == '__main__':
    unittest.main()