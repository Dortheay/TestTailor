import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'test_file.txt'
            str_1 = 'LINEMODE'
            var_0 = module_0.islurp(str_0, str_1, str_1)
            str_2 = '-'
            bool_0 = False
            var_1 = module_0.islurp(str_2, str_2, str_1, bool_0)
            var_2 = list(var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
