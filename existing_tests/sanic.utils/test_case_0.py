import unittest
import timeout_decorator
import sanic.utils as module_0
import pathlib as module_1
import _frozen_importlib_external as module_2

class Test_Utils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '\rESxV%i3e{;'
            bool_0 = module_0.str_to_bool(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
