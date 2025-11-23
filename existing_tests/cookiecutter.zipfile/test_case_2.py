import unittest
import timeout_decorator
import cookiecutter.zipfile as module_0

class Test_Zipfile_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'|\x04\xc7\xf1\xbc\xd5\xafI'
            tuple_0 = None
            var_0 = module_0.unzip(bytes_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
