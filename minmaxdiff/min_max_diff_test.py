import unittest
import min_max_diff

class TestMinMaxDiff(unittest.TestCase):
    def test_min_max_diff_with_empty_list(self):
        self.assertEqual(min_max_diff.min_max_diff([]), None)
    def test_min_max_diff_with_self(self):
        self.assertEqual(min_max_diff.min_max_diff([4,7,3,2,9]), 7)
    def test_min_max_diff_with_null(self):
        self.assertEqual(min_max_diff.min_max_diff([0]), 0)

if __name__ == '__main__':
    unittest.main()
