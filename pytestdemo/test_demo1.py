# any pytest file should start with test_ or end with  _test
# pytest method names should start with test
# any module name should start with pytest
# any code should be wrapped in method only

import unittest
import pytest
import pytestdemo


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


# if __name__ == '__main__':
#     unittest.main()

@pytest.mark.smoke
def test_first_program():
    print("Hello")


def test_second_program():
    print("Good Afternoon")


def test_cross_browser(cross_browser):
    print(cross_browser)