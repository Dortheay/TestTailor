import unittest
import timeout_decorator
import cookiecutter.repository as module_0

class Test_Repository_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bytes_0 = b'y\xdc4\xbd[\xc7\xe2'
            dict_0 = {bytes_0: bytes_0}
            var_0 = module_0.expand_abbreviations(bytes_0, dict_0)
            int_0 = 2
            float_0 = -508.27047
            tuple_0 = (int_0, float_0)
            var_1 = module_0.is_repo_url(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
