#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework 01: Testing triangle"""

# Requirements Specification: “Write a function classify_triangle() that takes three
# parameters: a, b, and c. The three parameters represent the lengths of the sides of a triangle.
# The function returns a string that specifies whether the triangle is scalene, isosceles,
# or equilateral, and whether it is a right triangle as well.”

__author__ = """Christopher Bischoff"""

# equilateral triangles have all three sides with the same length
# isosceles triangles have two sides with the same length
# scalene triangles have three sides with different lengths
# right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2

class classify_triangle:
    def __init__(self, x, y, z):

        if x <= 0 or y <= 0 or z <= 0:
            self.message = "ERROR:Not valid values for length"
            return

        # Side lengths do not adhere to the triangle inequality theorem.
        # which states that the sum of the side lengths of any 2 sides of a triangle
        # must exceed the length of the third side
        if x + y <= z or y + z <= x or z + x <= y:
            self.message = "ERROR:Not valid values for Triangle"
            return

        if z ^ 2 == (x ^ 2 + y ^ 2):
            self.message = "right"
            return

        if x == y and y == z:
            self.message = "equilateral"  # Three equal sides
            return
        elif x == y or x == z or y == z:
            self.message = "isosceles"  # Two equal sides
            return
        elif (x != y) and (x != z) and (y != z):
            self.message = "scalene"  # No equal sides
            return

if __name__ == '__main__':
    print("Input lengths of the triangle sides: ")
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    triangle = classify_triangle(x, y, z)
    print(triangle.message)
