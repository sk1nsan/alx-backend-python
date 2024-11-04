#!/usr/bin/env python3
""" Testing utilsl
"""

import unittest
from unittest.mock import patch, Mock
import utils
from utils import memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Testing access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, arg1, arg2, expected):
        """ testing with normal input"""
        self.assertEqual(utils.access_nested_map(arg1, arg2), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, arg1, arg2):
        """ testing with exception """
        with self.assertRaises(KeyError):
            utils.access_nested_map(arg1, arg2)


class TestGetJson(unittest.TestCase):
    """ Testing test_get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ testing with mock """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get",
                   return_value=Mock(**attrs)) as mock_requests:
            self.assertEqual(utils.get_json(test_url), test_payload)
            mock_requests.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Testing memoize """

    def test_memoize(self):
        """ testing memoize """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as mock:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mock.assert_called_once()
