#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework 04: Requirements Testing"""

# Requirements Specification: “Write a function classify_triangle() that takes three
# parameters: a, b, and c. The three parameters represent the lengths of the sides of a triangle.
# The function returns a string that specifies whether the triangle is scalene, isosceles,
# or equilateral, and whether it is a right triangle as well.”

__author__ = """Christopher Bischoff"""

# equilateral triangles have all three sides with the same length
# isosceles triangles have two sides with the same length
# scalene triangles have three sides with different lengths
# right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2

from decimal import *
getcontext().prec=30

class classify_triangle:
    def __init__(self, x, y, z):

        # Checking values are greater than Zero
        if x <= 0 or y <= 0 or z <= 0:
            self.message = "ERROR:All values must be greater than zero"
            return

        # Checking values are less than 1000 i.e "not to big"
        if x > 1000 or y > 1000 or z > 1000:
            self.message = "ERROR:All values must be less than 1000"
            return

        # Checking values are real numbers i.e not complex
        if (isinstance(x,complex ) or isinstance(y,complex ) or isinstance(z,complex )):
            self.message = "ERROR:All values must be a real number"
            return


        # Side lengths do not adhere to the triangle inequality theorem.
        # which states that the sum of the side lengths of any 2 sides of a triangle
        # must exceed the length of the third side
        if x + y <= z or y + z <= x or z + x <= y:
            self.message = "ERROR:Not valid values for Triangle"
            return

        # All Three sides equal
        if x == y and y == z:
            self.message = "Equilateral Triangle"  # Three equal sides
            return
            
        if (abs((z*z)- ((x*x) + (y*y)))) <= Decimal('0.012944'):
            if x == y or x == z or y == z:
                self.message = "Right Isosceles Triangle"  # Two equal sides
                return
            elif (x != y) and (x != z) and (y != z):
                self.message = "Right Scalene Triangle"  # No equal sides
                return

        if x == y or x == z or y == z:
            self.message = "Isosceles Triangle"  # Two equal sides
            return
        elif (x != y) and (x != z) and (y != z):
            self.message = "Scalene Triangle"  # No equal sides
            return


if __name__ == '__main__':
    print("Input lengths of the triangle sides: ")
    x = Decimal(input("A: "))
    y = Decimal(input("B: "))
    z = Decimal(input("C: "))

    triangle = classify_triangle(x, y, z)
    print(triangle.message)
