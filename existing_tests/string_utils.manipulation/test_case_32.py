import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_33(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            str_0 = None
            bool_0 = module_0.booleanize(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
