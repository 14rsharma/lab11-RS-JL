# https://github.com/14rsharma/lab11-RS-JL
# Partner 1: Raghav Sharma
# Partner 2: Jon-Paul Linter

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
  def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)

def test_subtract(self):
    self.assertEqual(subtract(5, 3), 2)
    self.assertEqual(subtract(3, 5), -2)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(4, 10), 2.5)
        self.assertAlmostEqual(div(5, 10), 2)
    # ##########################

    ######## Partner 2
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
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
