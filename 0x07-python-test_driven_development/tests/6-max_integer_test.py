import unittest
max_integer = __import__('6-max_integer').max_integer
"""a unittest for max_integer() function
"""
class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger inherits from the
        unittest.TestCase class

    Args:
        unittest (class): python class that help
            in code testing
    """
    def test_empty_list(self):
        """method that checks for an empty list
            passed to the 'max_integer()' function
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        """a method that tests for positive numbers
            in the 'max_integer()' function
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """a method that tests for negative numbers
            in the 'max_integer()' function
        """
        result = max_integer([-4, -2, -7, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """method that checks for list of integer
            type in the 'max_integer()' function
        """
        result = max_integer([-4, 2, -7, 0, 9])
        self.assertEqual(result, 9)

    def test_single_number(self):
        """method that checks for list with only the
            '0' index in the 'max_integer()' function
        """
        result = max_integer([42])
        self.assertEqual(result, 42)

if __name__ == "__main__":
    unittest.main()
