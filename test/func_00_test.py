import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from func_00 import func_00


class TestSRC01(unittest.TestCase):

    def test_func_01_without_arg(self):
        res = 0.123
        self.assertEqual(func_00(), res)

    def test_func_01_with_none(self):
        arg = None
        res = 0.123
        self.assertEqual(func_00(arg=arg), res)

    def test_func_01_with_null(self):
        arg = 0
        res = 0
        self.assertEqual(func_00(arg=arg), res)

        arg = 0.0
        res = 0.0
        self.assertEqual(func_00(arg=arg), res)

    def test_func_01_with_arg(self):
        arg = 9.876543210
        res = 9.876543210
        self.assertEqual(func_00(arg=arg), res)


if __name__ == "__main__":
    unittest.main()
