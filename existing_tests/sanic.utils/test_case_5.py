import unittest
import timeout_decorator
import sanic.utils as module_0
import pathlib as module_1
import _frozen_importlib_external as module_2

class Test_Utils_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            path_0 = module_1.Path()
            str_0 = 'j>{k,'
            list_0 = [path_0]
            var_0 = module_0.load_module_from_file_location(path_0, str_0, *list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
