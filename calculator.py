# https://github.com/14rsharma/lab11-RS-JL
# Partner 1: Raghav Sharma
# Partner 2: Jon-Paul Linter

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# Second Example
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b

#Part 2 Partner 2 
def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)

def test_subtract(self):
    self.assertEqual(subtract(5, 3), 2)
    self.assertEqual(subtract(3, 5), -2)

def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        div(0, 5)

def test_logarithm(self):
    self.assertAlmostEqual(logarithm(2, 8), 3)
    self.assertAlmostEqual(logarithm(10, 100), 2)

def test_log_invalid_base(self):
    with self.assertRaises(ValueError):
        logarithm(1, 8)
    with self.assertRaises(ValueError):
        logarithm(-2, 8)
