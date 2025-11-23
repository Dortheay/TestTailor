import unittest
import timeout_decorator
import cookiecutter.zipfile as module_0

class Test_Zipfile_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'hSe'
            bytes_0 = b'\x1e\x16y\xf8\x04\xe8\xaf8\xfd\n\xb5\xd4'
            var_0 = module_0.unzip(str_0, bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
