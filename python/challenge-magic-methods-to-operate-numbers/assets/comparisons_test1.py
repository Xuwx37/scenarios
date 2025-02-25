import unittest
import sys

sys.path.append("/home/labex/project")

from comparisons import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_eq(self):
        a = MathExpression(5)
        b = MathExpression(5)
        self.assertTrue(a == b)


if __name__ == "__main__":
    unittest.main()
