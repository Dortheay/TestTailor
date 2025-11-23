import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = '\t""\x0b\x0ci)2xlBjvM1'
        bool_0 = module_0.is_decimal(str_0)
        str_1 = 'c<BNt?uI\rH'
        bool_1 = module_0.contains_html(str_1)
        bool_2 = module_0.is_integer(str_1)
        bool_3 = module_0.is_isbn(str_1)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_1)

if __name__ == "__main__":
    unittest.main()
