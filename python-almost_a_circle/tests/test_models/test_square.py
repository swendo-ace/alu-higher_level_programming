#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_inherits_rectangle(self):
        """Square is a subclass of Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_size_sets_both(self):
        """size sets width and height."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_area(self):
        """Area is size squared."""
        self.assertEqual(Square(5).area(), 25)

    def test_size_getter(self):
        """size getter returns width."""
        self.assertEqual(Square(7).size, 7)

    def test_size_setter(self):
        """size setter updates width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_not_int(self):
        """Non-int size raises TypeError."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero(self):
        """Size of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """__str__ format is correct."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_update_args(self):
        """update with args."""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_update_kwargs(self):
        """update with kwargs."""
        s = Square(5)
        s.update(size=7, x=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 1)

    def test_to_dictionary(self):
        """to_dictionary returns the right dict."""
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 5, "size": 10, "x": 2, "y": 1})


if __name__ == "__main__":
    unittest.main()
