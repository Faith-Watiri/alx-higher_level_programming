#!/usr/bin/python3
"""
unit tests
"""

import unittest

class TestBase(unittest.TestCase):
    """Base class tests"""
    def _too_many_args(self):
        """testing args"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def _no_id(self):
        """Testing id as None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def _id_set(self):
        """Testing id as nt None"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def _no_id_after_set(self):
        """Testin id as None after not None"""
        b2 = Base()
        self.assertEqual(b2.id, 2)


