#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_given(self):
        """An explicit id is kept."""
        self.assertEqual(Base(12).id, 12)

    def test_id_auto(self):
        """An auto id is an integer."""
        self.assertIsInstance(Base().id, int)

    def test_id_sequence(self):
        """Auto ids increment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_none(self):
        """None gives '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Empty list gives '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_data(self):
        """A list of dicts is JSON encoded."""
        s = Base.to_json_string([{"id": 1}])
        self.assertEqual(s, '[{"id": 1}]')

    def test_from_json_string_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_data(self):
        """A JSON string is decoded to a list."""
        r = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(r, [{"id": 1}])


if __name__ == "__main__":
    unittest.main()
