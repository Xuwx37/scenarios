import sys

sys.path.append("/home/labex/project")
import unittest
from simple_calculator import simple_calculator


class TestStep2(unittest.TestCase):
    def test_valid_input(self):
        result = simple_calculator().validate_user_input("10", "5", "+")
        self.assertEqual(result, None)

    def test_invalid_input(self):
        result = simple_calculator().validate_user_input("abc", "def", "@")
        self.assertEqual(result, "Please enter valid numbers")


if __name__ == "__main__":
    unittest.main()
