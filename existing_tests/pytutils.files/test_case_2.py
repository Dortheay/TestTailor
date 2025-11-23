import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '~/file.txt'
            str_1 = 'w'
            bool_0 = True
            var_0 = module_0.burp(str_0, str_1, str_1, bool_0, bool_0)
            str_2 = '/mock/env/file.txt'
            str_3 = '-'
            str_4 = 'example contents'
            bool_1 = True
            var_1 = module_0.burp(str_3, str_4, str_2, bool_1)
            str_5 = 'file.txt'
            bool_2 = False
            var_2 = module_0.burp(str_5, str_4, str_4, bool_2, bool_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
