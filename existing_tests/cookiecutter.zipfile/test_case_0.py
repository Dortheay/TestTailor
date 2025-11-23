import unittest
import timeout_decorator
import cookiecutter.zipfile as module_0

class Test_Zipfile_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = -4047.0
            bool_0 = False
            var_0 = module_0.unzip(float_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
