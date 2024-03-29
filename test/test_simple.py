# coding: utf-8

"""
    MultiWoven API

    Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from multiwoven_python_sdk import Multiwoven

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        multiwoven = Multiwoven(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(multiwoven)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
