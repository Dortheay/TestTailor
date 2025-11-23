import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'a]yi'
            int_0 = module_0.roman_decode(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
