#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_inherits_base(self):
        """Rectangle is a subclass of Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_attributes(self):
        """Attributes are set correctly."""
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        """Area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_width_not_int(self):
        """Non-int width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_not_int(self):
        """Non-int height raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_zero(self):
        """Width of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_negative(self):
        """Negative height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_negative(self):
        """Negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_negative(self):
        """Negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_str(self):
        """__str__ format is correct."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """update with args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update with kwargs."""
        r = Rectangle(10, 10)
        r.update(width=1, height=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_to_dictionary(self):
        """to_dictionary returns the right dict."""
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 5, "width": 10, "height": 2,
                             "x": 1, "y": 9})


if __name__ == "__main__":
    unittest.main()
