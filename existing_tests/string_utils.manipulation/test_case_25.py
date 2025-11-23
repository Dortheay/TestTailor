import unittest
import timeout_decorator
import string_utils.manipulation as module_0

class Test_Manipulation_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = '\x0b|'
            str_1 = ';R'
            bool_0 = module_0.booleanize(str_1)
            str_2 = module_0.shuffle(str_0)
            str_3 = module_0.strip_html(str_1)
            str_4 = module_0.decompress(str_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
