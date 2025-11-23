import unittest
import timeout_decorator
import sanic.utils as module_0
import pathlib as module_1
import _frozen_importlib_external as module_2

class Test_Utils_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'mock'
            str_1 = '/test/path/mock.py'
            var_0 = module_2.spec_from_file_location(str_0, str_1)
            str_2 = '/test/path/${TEST_VAR}/mock.py'
            var_1 = module_0.load_module_from_file_location(str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
