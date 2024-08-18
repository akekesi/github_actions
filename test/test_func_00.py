import coverage
import unittest

from src.func_00 import func_00


class TestFunc00(unittest.TestCase):

    def test_func_00_without_arg(self):
        res = 0.123
        self.assertEqual(func_00(), res)

    def test_func_00_with_none(self):
        arg = None
        res = 0.123
        self.assertEqual(func_00(arg=arg), res)

    def test_func_00_with_null(self):
        arg = 0
        res = 0
        self.assertEqual(func_00(arg=arg), res)

        arg = 0.0
        res = 0.0
        self.assertEqual(func_00(arg=arg), res)

    def test_func_00_with_arg(self):
        arg = 9.876543210
        res = 9.876543210
        self.assertEqual(func_00(arg=arg), res)

    # def test_func_00_with_err(self):
    #     arg = "9.876543210"
    #     res = 9.876543210
    #     self.assertEqual(func_00(arg=arg), res)


if __name__ == "__main__": # pragma: no cover
    cov = coverage.Coverage()
    cov.start()

    try:
        unittest.main()
    except:  # catch-all except clause
        pass

    cov.stop()
    cov.save()

    cov.html_report()
