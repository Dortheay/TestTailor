import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = ''
        bool_0 = False
        bool_1 = module_0.is_isbn(str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
