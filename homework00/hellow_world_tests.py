#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework-00: HelloWorld"""

__author__ = """Christopher Bischoff"""

import unittest
from hellow_world import Hellow

class HelloWorldTests(unittest.TestCase):
    def test_hello(self):
        hellow_object = Hellow()
        self.assertEqual(hellow_object.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()
