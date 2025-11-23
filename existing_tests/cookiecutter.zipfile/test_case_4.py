import unittest
import timeout_decorator
import cookiecutter.zipfile as module_0

class Test_Zipfile_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'http://docs.python.org/'
            bytes_0 = b'\xfa\xc8\x11\x16l\x86\x9c\xaf\xb5z'
            var_0 = module_0.unzip(str_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
