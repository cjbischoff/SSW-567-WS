# Homework 01: Testing triangle classification

## Requirements Specification:

“Write a function classify_triangle() that takes three  parameters: a, b, and c. The three parameters represent the lengths of the sides of a triangle. The function returns a string that specifies whether the triangle is scalene, isosceles, or equilateral, and whether it is a right triangle as well.”

## Assignment Deliverables:

### Deliverable 1:

Upload a file with Python or Java source code for your classify triangle solution to Canvas.  The file should include the source code used to solve the problem and the test cases for the code.  Your test cases should demonstrate that you've adequately tested your solution.

### Deliverable 2:

Upload a text file or screen shot to show the input and output of running the program and demonstrating that your program has been adequately tested.

### Deliverable 3:

Describe your experience with this assignment, specifically:

**1.**  What challenges did you encounter with the task definition?

I was not provide specific/clear requirements:

- I was told to input parameters, but didn't  the requirements were not specific whether it would be integer or decimal parameter (I assumed integer).
- I was not told to check for bad-data either improper length data or data that could not be a triangle (I created logic to test for that data and subsequent tests).
- I received "mixed" requirements; equilateral, isosceles, and scalene are triangle classifications based upon the length of sides, but right (acute and obtuse) are triangle classification based upon angles. For example a triangle can be classified as  Right Isosceles. (I did not solve for the Right Triangle)

**2.** What challenges did you encounter with the tools?

No real challenges with the tools, I had to write not an optimized solution to meet the homework requirement.  Would have easier to write just a class/function and then the test cases vs the class/function with a main for the driver (to meet deliverable 2).  I guess I could have wrote 3x pieces code:

- the class/function
- the unit testes
- a driver to call and run a loop to show it functions

**3.** Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?

I didn't have any criteria, I found an online triangle calculator site and inputed values to find possible lengths to triangle classification.  I ensure I had data for at least each requirement and also for bad data (not a triangle/bad lengths)

#### reference

- equilateral triangles have all three sides with the same length
- isosceles triangles have two sides with the same length
- scalene triangles have three sides with different lengths
- right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
