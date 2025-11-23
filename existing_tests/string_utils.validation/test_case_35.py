import unittest
import timeout_decorator
import string_utils.validation as module_0

class Test_Validation_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_25(self):
        str_0 = 'tM~rIcnUr'
        bool_0 = module_0.contains_html(str_0)

if __name__ == "__main__":
    unittest.main()
