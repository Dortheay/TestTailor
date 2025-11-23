import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = None
            bool_0 = module_0.contains_html(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
