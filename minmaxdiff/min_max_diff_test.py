import unittest
from min_max_diff import min_max_diff

class TestMinMaxDiff(unittest.TestCase):
    def test_min_max_diff_with_empty_list(self):
        self.assertEqual(min_max_diff([]), None)
    def test_min_max_diff_with_self(self):
        self.assertEqual(min_max_diff([4,7,3,4,14]), 11)
    def test_min_max_diff_with_two_numbers(self):
        self.assertEqual(min_max_diff([22,17]), 5)

if __name__ == '__main__':
    unittest.main()
