import coverage
import unittest
import inspect

from typing import Optional

# try importing the function
try:
    from src.func_00 import func_00
except (ImportError, ModuleNotFoundError) as e:
    func_00 = None
    IMPORT_ERROR = e
else:
    IMPORT_ERROR = None


class TestFunc00(unittest.TestCase):

    def test_func_00_exists(self):
        """Ensure that func_00 is defined and callable."""
        self.assertIsNone(IMPORT_ERROR, f"Import failed: {IMPORT_ERROR}")
        self.assertTrue(callable(func_00), "func_00 is not callable")

    def test_func_00_has_signature(self):
        """Check that func_00 has the correct signature."""
        sig = inspect.signature(func_00)

        # Check parameter names
        self.assertEqual(list(sig.parameters.keys()), ['arg'])

        # Check default value and annotation
        param = sig.parameters['arg']
        self.assertEqual(param.default, None)
        self.assertEqual(param.annotation, Optional[float])

        # Check return annotation
        self.assertEqual(sig.return_annotation, float)

    def test_func_00_without_arg(self):
        """Test func_00 without any arguments."""
        res = 0.123
        self.assertEqual(func_00(), res)

    def test_func_00_with_none(self):
        """Test func_00 with None as argument."""
        arg = None
        res = 0.123
        self.assertEqual(func_00(arg=arg), res)

    def test_func_00_with_null(self):
        """Test func_00 with 0 and 0.0 as arguments."""
        arg = 0
        res = 0
        self.assertEqual(func_00(arg=arg), res)

        arg = 0.0
        res = 0.0
        self.assertEqual(func_00(arg=arg), res)

    def test_func_00_with_arg(self):
        """Test func_00 with a float argument."""
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
    except Exception as e:
        print(f"Error running tests: {e}")

    cov.stop()
    cov.save()

    cov.html_report()
