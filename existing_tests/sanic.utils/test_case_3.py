import unittest
import timeout_decorator
import sanic.utils as module_0
import pathlib as module_1
import _frozen_importlib_external as module_2

class Test_Utils_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'\xcd\x1e\x9f\x06\xb5Z\\\xccG'
            var_0 = module_0.load_module_from_file_location(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
