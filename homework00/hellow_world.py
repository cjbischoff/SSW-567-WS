#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework-00: HelloWorld"""

__author__ = """Christopher Bischoff"""

import sys

class Hellow:
    def __init__(self):
        self.message = "Hello world!"

if __name__ == '__main__':
    hellow_world = Hellow()
    print(hellow_world.message)