import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = '-'
            str_1 = 'Test to stdout'
            str_2 = 'w'
            bool_0 = True
            var_0 = module_0.burp(str_0, str_1, str_2, bool_0)
            str_3 = '$TEST_VAR_file.txt'
            str_4 = 'Variable expansion test'
            bool_1 = True
            var_1 = module_0.burp(str_3, str_4, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
