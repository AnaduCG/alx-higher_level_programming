import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        result = max_integer([-4, -2, -7, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-4, 2, -7, 0, 9])
        self.assertEqual(result, 9)

    def test_single_number(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

if __name__ == "__main__":
    unittest.main()
