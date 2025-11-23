import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            str_0 = '`4("308\t]v85'
            dict_0 = {}
            string_compressor_0 = module_0.__StringCompressor(**dict_0)
            str_1 = module_0.strip_html(str_0)
            str_2 = '^3[47]\\d{13}$'
            int_0 = 339
            str_3 = module_0.compress(str_2, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
