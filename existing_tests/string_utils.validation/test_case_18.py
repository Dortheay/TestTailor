import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        str_0 = 'PJ,oq,/#Ex'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        tuple_0 = (i_s_b_n_checker_0,)
        bool_0 = module_0.is_camel_case(tuple_0)
        str_1 = 'Tq{7H.\\Sh'
        bool_1 = module_0.is_decimal(str_1)
        str_2 = 'q6]0R"B9'
        bool_2 = module_0.is_isbn_13(str_2)

if __name__ == "__main__":
    unittest.main()
