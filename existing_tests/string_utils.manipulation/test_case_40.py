import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_41(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_29(self):
        try:
            str_0 = ' '
            str_1 = module_0.snake_case_to_camel(str_0)
            str_2 = 'c'
            str_3 = '4|HTOuVbtu\x0c}'
            int_0 = None
            str_4 = module_0.compress(str_2, str_3, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
