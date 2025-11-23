import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = '~/file.txt'
            str_1 = 'w'
            bool_0 = True
            var_0 = module_0.burp(str_0, str_1, str_1, bool_0, bool_0)
            str_2 = '/mock/env/file.txt'
            str_3 = '-'
            str_4 = 'example contents'
            bool_1 = False
            var_1 = module_0.burp(str_3, str_4, str_2, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
