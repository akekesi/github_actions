import coverage
import unittest

from src.class_00 import Class00


class TestClass00(unittest.TestCase):
    def setUp(self):
        self.config = {
            'a': 0.123456789
        }

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
