import unittest
import timeout_decorator
import cookiecutter.find as module_0

class Test_Find_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            complex_0 = None
            var_0 = module_0.find_template(complex_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
