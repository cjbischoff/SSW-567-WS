#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework 01: Testing triangle"""

__author__ = """Christopher Bischoff"""

import unittest

from classify_triangle import classify_triangle


class ClassifyTriangleTests(unittest.TestCase):

    def testEquilateral1(self):
        triangle_object = classify_triangle(2, 2, 2)
        self.assertEquals(triangle_object.message, 'equilateral')

    def testEquilateral2(self):
        triangle_object = classify_triangle(10, 10, 10)
        self.assertEquals(triangle_object.message, 'equilateral')

    def testIsosceles1(self):
        triangle_object = classify_triangle(4, 5, 5)
        self.assertEquals(triangle_object.message, 'isosceles')

    def testIsosceles2(self):
        triangle_object = classify_triangle(4, 4, 3)
        self.assertEquals(triangle_object.message, 'isosceles')

    def testIsosceles3(self):
        triangle_object = classify_triangle(10, 10, 2)
        self.assertEquals(triangle_object.message, 'isosceles')

    def testInvalidLength1(self):
        triangle_object = classify_triangle(-1, 1, 1)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for length')

    def testInvalidLength2(self):
        triangle_object = classify_triangle(7, 3, 2)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for length')

    def testInvalidLength3(self):
        triangle_object = classify_triangle(2, 4, 2)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for length')

    def testRight(self):
        triangle_object = classify_triangle(4, 5, 5)
        self.assertEquals(triangle_object.message, 'right')

    def testScalene1(self):
        triangle_object = classify_triangle(4, 5, 8)
        self.assertEquals(triangle_object.message, 'scalene')

    def testScalene2(self):
        triangle_object = classify_triangle(5, 4, 2)
        self.assertEquals(triangle_object.message, 'scalene')


if __name__ == '__main__':
    unittest.main()
