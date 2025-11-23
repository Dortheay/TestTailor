import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'E3>\x0c)q[G@\r@v#'
            bool_0 = False
            bool_1 = module_0.is_json(bool_0)
            bool_2 = True
            bool_3 = module_0.is_isbn(str_0, bool_2)
            str_1 = 'compress'
            bool_4 = None
            bool_5 = module_0.is_isbn_13(str_1, bool_4)
            bool_6 = module_0.is_credit_card(bool_3)
            bool_7 = module_0.is_isbn(str_0)
            str_2 = '2'
            bool_8 = module_0.is_isbn_13(str_0)
            bool_9 = module_0.is_credit_card(str_2, str_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
