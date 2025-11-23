import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        str_0 = 'v&5H}1LF?L( |##'
        bool_0 = module_0.is_uuid(str_0)
        bool_1 = True
        bool_2 = module_0.is_isbn_10(str_0, bool_1)
        bool_3 = module_0.is_json(bool_2)
        bool_4 = module_0.is_json(str_0)
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_5 = module_0.is_full_string(i_s_b_n_checker_0)

if __name__ == "__main__":
    unittest.main()
