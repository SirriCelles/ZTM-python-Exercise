# pylint
# pyflakes
# PEP 8

import unittest
import main_test


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main_test.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'somestring'
        result = main_test.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main_test.do_stuff(test_param)
        self.assertEqual(result, 'Please Enter a number')


if __name__ == '__main__':
    unittest.main()
