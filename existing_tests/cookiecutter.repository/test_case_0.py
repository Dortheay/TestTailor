import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 781
            var_0 = module_0.is_zip_file(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
