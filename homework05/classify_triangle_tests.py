#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework 05 - Design and Unit Testing"""

__author__ = """Christopher Bischoff"""

import unittest

from classify_triangle import classify_triangle


class ClassifyTriangleTests(unittest.TestCase):
    def test_Boundary_1(self):
        """Boundary Conditions T1"""
        triangle_object = classify_triangle(1, 1, 1)
        self.assertEquals(triangle_object.message,
                          'Equilateral Triangle')

    def test_T1_1(self):
        """Homework04 TestCase"""
        """Boundary Conditions T2"""
        triangle_object = classify_triangle(0, 1, 1)
        self.assertEquals(triangle_object.message,
                          'ERROR:All values must be greater than zero')

    def test_T1_2(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(1, 0, 1)
        self.assertEquals(triangle_object.message,
                          'ERROR:All values must be greater than zero')

    def test_T1_3(self):
        """Homework04 TestCase"""
        """Boundary Conditions T3"""
        triangle_object = classify_triangle(1, 1, 0)
        self.assertEquals(triangle_object.message,
                          'ERROR:All values must be greater than zero')

    def test_T2_1(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(1001, 1, 1)
        self.assertEquals(
            triangle_object.message,
            'ERROR:All values must be less than 1000')

    def test_T2_2(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(1, 1001, 1)
        self.assertEquals(
            triangle_object.message,
            'ERROR:All values must be less than 1000')

    def test_T2_3(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(1, 1, 1001)
        self.assertEquals(
            triangle_object.message,
            'ERROR:All values must be less than 1000')

    def test_T4_1(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(7, 3, 2)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for Triangle')

    def test_T4_2(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(2, 4, 2)
        self.assertEquals(triangle_object.message,
                          'ERROR:Not valid values for Triangle')

    def test_T4_3(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(4, 5, 5e10)
        self.assertEquals(
            triangle_object.message,
            'ERROR:All values must be less than 1000')

    def test_T5_1(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(
            1, 1, 1.4142135623730950488016887241)
        self.assertEquals(triangle_object.message, 'Right Isosceles Triangle')

    def test_T5_2(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(10.1, 20.2, 22.584)
        self.assertEquals(triangle_object.message, 'Right Scalene Triangle')

    def test_T6_1(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(2, 2, 2)
        self.assertEquals(triangle_object.message, 'Equilateral Triangle')

    def test_T6_2(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(10, 10, 10)
        self.assertEquals(triangle_object.message, 'Equilateral Triangle')

    def test_T11_1(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(4, 5, 5)
        self.assertEquals(triangle_object.message, 'Isosceles Triangle')

    def test_T11_2(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(4, 4, 3)
        self.assertEquals(triangle_object.message, 'Isosceles Triangle')

    def test_T11_3(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(10, 10, 2)
        self.assertEquals(triangle_object.message, 'Isosceles Triangle')

    def test_T11_4(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(4, 5, 5)
        self.assertEquals(triangle_object.message, 'Isosceles Triangle')

    def test_T9_1(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(4, 5, 8)
        self.assertEquals(triangle_object.message, 'Scalene Triangle')

    def test_T9_2(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(5, 4, 2)
        self.assertEquals(triangle_object.message, 'Scalene Triangle')

    def test_T9_3(self):
        """Homework04 TestCase"""
        triangle_object = classify_triangle(5e-51, 4e-51, 3e-51)
        self.assertEquals(triangle_object.message, 'Right Scalene Triangle')


if __name__ == '__main__':
    unittest.main()
