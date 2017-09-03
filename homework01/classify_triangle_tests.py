#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework 01: Testing triangle"""

__author__ = """Christopher Bischoff"""

import unittest

from classify_triangle import classify_triangle


class ClassifyTriangleTests(unittest.TestCase):

    def test1(self):
        triangle_object = classify_triangle(2, 2, 2)
        self.assertEquals(triangle_object.message, 'equilateral')

    def test2(self):
        triangle_object = classify_triangle(10, 10, 10)
        self.assertEquals(triangle_object.message, 'equilateral')

    def test3(self):
        triangle_object = classify_triangle(4, 5, 5)
        self.assertEquals(triangle_object.message, 'isosceles')

    def test4(self):
        triangle_object = classify_triangle(4, 4, 3)
        self.assertEquals(triangle_object.message, 'isosceles')

    def test5(self):
        triangle_object = classify_triangle(10, 10, 2)
        self.assertEquals(triangle_object.message, 'isosceles')

    def test6(self):
        triangle_object = classify_triangle(-1, 1, 1)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for length')

    def test7(self):
        triangle_object = classify_triangle(7, 3, 2)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for Triangle')

    def test8(self):
        triangle_object = classify_triangle(2, 4, 2)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for Triangle')

    def test9(self):
        triangle_object = classify_triangle(4, 5, 5)
        self.assertEquals(triangle_object.message, 'isosceles')

    def test10(self):
        triangle_object = classify_triangle(4, 5, 8)
        self.assertEquals(triangle_object.message, 'scalene')

    def test11(self):
        triangle_object = classify_triangle(5, 4, 2)
        self.assertEquals(triangle_object.message, 'scalene')

    def test12(self):
        triangle_object = classify_triangle(-5, 4, 3)
        self.assertEquals(triangle_object.message, 'ERROR:Not valid values for length')

    def test13(self):
        triangle_object = classify_triangle(-1, 1, 3)
        self.assertEquals(triangle_object.message, 'ERROR:Not valid values for length')

    def test14(self):
        triangle_object = classify_triangle(-5, 4, 3)
        self.assertEquals(triangle_object.message, 'ERROR:Not valid values for length')


    def test15(self):
        triangle_object = classify_triangle(5e-51,4e-51,3e-51)
        self.assertEquals(triangle_object.message, 'scalene')

    def test16(self):
        triangle_object = classify_triangle(4,5,5e10)
        self.assertEquals(triangle_object.message, 'ERROR:Not valid values for Triangle')

    def test17(self):
        triangle_object = classify_triangle(1,1,1.4142135623730950488016887241)
        self.assertEquals(triangle_object.message, 'right')

    def test18(self):
        triangle_object = classify_triangle(10.1,20.2,22.584)
        self.assertEquals(triangle_object.message, 'right')

if __name__ == '__main__':
    unittest.main()
