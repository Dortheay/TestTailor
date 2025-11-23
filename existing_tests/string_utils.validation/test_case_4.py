import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = 'd0W9x'
            bool_0 = module_0.contains_html(str_0)
            str_1 = None
            int_0 = module_0.words_count(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
