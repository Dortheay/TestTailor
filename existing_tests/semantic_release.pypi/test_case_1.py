import unittest
import timeout_decorator
import semantic_release.pypi as module_0

class Test_Pypi_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'z+'
            bool_0 = False
            list_0 = [str_0]
            var_0 = module_0.upload_to_pypi(str_0, bool_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
