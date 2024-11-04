#!/usr/bin/env python3
""" Testing utilsl
"""

import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Test Class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, arg1, arg2, expected):
        """ testing access_nested_map function """
        self.assertEqual(utils.access_nested_map(arg1, arg2), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, arg1, arg2):
        """ testing test_access_nested_map_exception function """
        with self.assertRaises(KeyError):
            utils.access_nested_map(arg1, arg2)
