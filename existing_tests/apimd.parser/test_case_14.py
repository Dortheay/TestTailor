import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        str_0 = 'h4'
        int_0 = 23
        int_1 = 2914
        bool_0 = module_0.is_public_family(str_0)
        dict_0 = {str_0: int_0, str_0: int_1}
        dict_1 = {}
        set_0 = set()
        str_1 = ']\tR'
        dict_2 = {str_0: set_0, str_1: set_0}
        parser_0 = module_0.Parser(dict_0, dict_1, dict_2)
        str_2 = parser_0.compile()
        bool_1 = module_0.is_magic(str_0)

if __name__ == "__main__":
    unittest.main()
