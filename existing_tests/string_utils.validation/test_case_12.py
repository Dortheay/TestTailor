import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'I[FI!|ujy\\.(P'
        i_s_b_n_checker_0 = module_0.__ISBNChecker(str_0)
        bool_0 = i_s_b_n_checker_0.is_isbn_13()

if __name__ == "__main__":
    unittest.main()
