import unittest
import timeout_decorator
import cookiecutter.zipfile as module_0

class Test_Zipfile_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = 'wK/oOx%n*=KY]Hn-'
            var_0 = module_0.unzip(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
