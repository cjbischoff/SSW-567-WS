#!/usr/bin/env python
# coding:utf-8

"""SSW-567-WS: Homework 01: Testing triangle"""

# Requirements Specification: “Write a function classify_triangle() that takes three
# parameters: a, b, and c. The three parameters represent the lengths of the sides of a triangle.
# The function returns a string that specifies whether the triangle is scalene, isosceles,
# or equilateral, and whether it is a right triangle as well.”

__author__ = """Christopher Bischoff"""

#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal

class classify_triangle:
    def __init__(self,x,y,z):


        if x <= 0 or y <= 0 or z <= 0:
            self.message = "ERROR:Not valid values for length"

        if x + y <= z or y+z <= z or z+x <= y:
            self.message = "ERROR:Not valid values for Triangle"

        if x == y and y == z:
            self.message = "equilateral"

        if x == y or x== z or y == z:
            self.message = "isosceles"

        length_difference = y - (x+y)
        if (length_difference == 0):
            self.message = "right"

        if (not (x == y or x== z or y == z)) and not(length_difference == 0):
            self.message = "scalene"


if __name__ == '__main__':
    print("Input lengths of the triangle sides: ")
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    triangle = classify_triangle(x,y,z)
    print(triangle.message)
