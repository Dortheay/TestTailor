import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            attribute_0 = module_0.Attribute()
            str_0 = None
            int_0 = -1572
            bool_0 = False
            dict_0 = {}
            assign_0 = module_0.Assign(**dict_0)
            str_1 = "@,wO\n'F\\nD(sF}a%lO"
            str_2 = '\x0cee'
            dict_1 = {str_1: str_2}
            parser_0 = module_1.Parser(int_0, bool_0, dict_1, dict_1)
            bool_1 = parser_0.is_public(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
