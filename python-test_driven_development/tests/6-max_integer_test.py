#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max at the end of an ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle of an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the start of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """A one-element list returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses the empty default and returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Works with all negative numbers."""
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_mixed_numbers(self):
        """Works with a mix of positive and negative."""
        self.assertEqual(max_integer([-5, 0, 5, 3]), 5)

    def test_floats(self):
        """Works with float values."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_duplicates(self):
        """Handles repeated max values."""
        self.assertEqual(max_integer([4, 4, 2, 1]), 4)


if __name__ == "__main__":
    unittest.main()
