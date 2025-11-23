import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_38(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        str_0 = 'V'
        bool_0 = module_0.is_json(str_0)

if __name__ == "__main__":
    unittest.main()
