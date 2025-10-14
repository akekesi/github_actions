import coverage
import unittest

# Try importing Class00 safely
try:
    from src.class_00 import Class00
except (ImportError, ModuleNotFoundError) as e:
    Class00 = None
    IMPORT_ERROR = e
else:
    IMPORT_ERROR = None


class TestClass00(unittest.TestCase):

    def setUp(self):
        self.config = {
            'a': 0.123456789
        }

    def test_class_00_exists(self):
        """Ensure that Class00 is successfully imported and is a class."""
        self.assertIsNone(IMPORT_ERROR, f"Import failed: {IMPORT_ERROR}")
        self.assertTrue(callable(Class00), "Class00 is not callable (not a class)")

    def test_class_00_class(self):
        class_00 = Class00(config=self.config)
        res_a = 0.123456789
        res_b = 0.0
        self.assertEqual(class_00.a, res_a)
        self.assertEqual(class_00.b, res_b)

    def test_class_00_func(self):
        class_00 = Class00(config=self.config)
        class_00.func_00()
        res_a = 0.123456789
        res_b = 0.123456789
        self.assertEqual(class_00.a, res_a)
        self.assertEqual(class_00.b, res_b)


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
