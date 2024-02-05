#!usr/bin/env python3
"""A module for testing utils module"""

import unittest
from parameterized import parameterized
from your_module import utils  # Replace 'your_module' with the actual module name

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected_result)

if __name__ == "__main__":
    unittest.main()
