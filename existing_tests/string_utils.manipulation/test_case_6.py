import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        str_0 = '-w'
        str_1 = module_0.strip_html(str_0)

if __name__ == "__main__":
    unittest.main()
