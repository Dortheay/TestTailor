import unittest
import timeout_decorator
import cookiecutter.zipfile as module_0

class Test_Zipfile_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'https://example.com/repo.zip'
            bool_0 = True
            bool_1 = False
            var_0 = None
            str_1 = './test_dir'
            var_1 = module_0.unzip(str_0, bool_0, str_1, bool_1, var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
