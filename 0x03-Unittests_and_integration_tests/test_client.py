#!/usr/bin/env python3
""" Testing client
"""

import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """ Testing GithubOrgClient"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, expected: Dict, mock_json: Mock) -> None:
        """ Testing org method """
        mock_json.return_value = Mock(return_value=expected)
        gh = GithubOrgClient(org)
        self.assertEqual(gh.org(), expected)
        mock_json.assert_called_once()
