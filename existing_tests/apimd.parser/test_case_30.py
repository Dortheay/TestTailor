import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            str_0 = 'h4'
            assign_0 = module_0.Assign()
            str_1 = 'EVDm?^'
            list_0 = [str_0, assign_0, str_0]
            attribute_0 = module_0.Attribute()
            dict_0 = {str_0: str_0, str_0: list_0, str_1: attribute_0}
            expr_0 = module_0.expr(**dict_0)
            list_1 = [expr_0, expr_0, expr_0, expr_0]
            list_2 = None
            bool_0 = True
            int_0 = None
            dict_1 = {str_0: int_0, str_0: int_0}
            dict_2 = {}
            parser_0 = module_1.Parser(bool_0, dict_1, dict_2)
            parser_0.class_api(str_1, str_1, list_1, list_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
