# Homework 05 - Design and Unit Testing

## Part 1:  The equivalence classes and boundary conditions for both inputs and outputs;

### Triangle Requirements from Module 4

**Possible Outputs**

1. Not a Legal triangle
2. Not Valid numbers
3. Right Scalene Triangle
4. Equilateral Triangle
5. Isosceles Triangle
6. Right Isosceles Triangle

### Equivalence Classes

| Test Case | x  | y  | z             | Output                   |
|-----------|----|----|---------------|--------------------------|
| T1        | 7  | 3  | 2             | Not a Legal triangle     |
| T2        | 0  | 1  | 1             | Not Valid numbers        |
| T3        | 3  | 4  | 5             | Right Scalene Triangle   |
| T4        | 1  | 1  | 1             | Equilateral Triangle     |
| T5        | 10 | 10 | 5             | Isosceles Triangle       |
| T6        | 2  | 2  | 2.82842712475 | Right Isosceles Triangle |

### Boundary Conditions

| Test Case | x      | y      | z      | Output               |
|-----------|--------|--------|--------|----------------------|
| T1        | 1      | 1      | 1      | Equilateral Triangle |
| T2        | 0      | 1      | 1      | Not Valid numbers    |
| T3        | 1      | 0      | 1      | Not Valid numbers    |
| T4        | 1      | 1      | 0      | Not Valid numbers    |
| T5        | 1e-100 | 1e-100 | 1e-100 | Not Valid numbers    |
| T6        | 7      | 3      | 2      | Not a Legal triangle |

## Part 2:  The test cases and test results that test those equivalence and boundary conditions;
## Part 3:  Identify both your original test cases and new test cases that you created to meet the equivalence class, boundary conditions, and/or coverage tests.


## Part 4:  The name and output of the static code analyzer tool you used;

### pylint and autopep8

I used the [pylint](https://www.pylint.org/) to perform the static analysis, after the initial run I used [autopep8](https://pypi.python.org/pypi/autopep8) to automatically correct formatting errors.

### First run

The first run, I am providing a summarized output:

```Your code has been rated at -5.25/10 (previous run: -5.25/10, +0.00)```


### Second run

**After performing the autopep8 auto correct:**

```
************* Module classify_triangle
W: 18, 0: Wildcard import decimal (wildcard-import)
C: 22, 0: Invalid class name "classify_triangle" (invalid-name)
C: 22, 0: Old-style class defined. (old-style-class)
C: 24, 4: Invalid argument name "x" (invalid-name)
C: 24, 4: Invalid argument name "y" (invalid-name)
C: 24, 4: Invalid argument name "z" (invalid-name)
R: 24, 4: Too many return statements (9/6) (too-many-return-statements)
R: 22, 0: Too few public methods (0/2) (too-few-public-methods)
C: 76, 4: Invalid constant name "triangle" (invalid-name)
W: 18, 0: Unused import BasicContext from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import InvalidContext from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import Underflow from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import DecimalException from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import DivisionByZero from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import localcontext from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_DOWN from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_HALF_EVEN from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_HALF_UP from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import re from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_UP from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import Inexact from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ConversionSyntax from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_FLOOR from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import DivisionImpossible from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import DecimalTuple from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import Overflow from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import local from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_HALF_DOWN from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import sys from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import InvalidOperation from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import DefaultContext from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import Context from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_05UP from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ROUND_CEILING from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import MockThreading from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import Subnormal from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import Rounded from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import ExtendedContext from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import threading from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import doctest from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import DivisionUndefined from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import setcontext from wildcard import (unused-wildcard-import)
W: 18, 0: Unused import Clamped from wildcard import (unused-wildcard-import)

--------------------------------------------------------------------
Your code has been rated at -0.75/10 (previous run: -0.75/10, +0.00)
```

## Part 5:  The name and output of the code coverage tool you used

### coverage.py

I used to the tool [Coverage.py](https://coverage.readthedocs.io/en/coverage-4.4.1/) and here is the first run of the tool on unmodified code/test-cases

```
coverage report -m                                                                                                                                                                                                                                              ✭ ✱ ◼ (git:create/homework05)
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
classify_triangle.py            41      8    80%   38-39, 70-76
classify_triangle_tests.py      67      0   100%
----------------------------------------------------------
TOTAL                          108      8    93%
```
