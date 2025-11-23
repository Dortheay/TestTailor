import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        str_0 = 'D^C1'
        set_0 = set()
        set_1 = None
        str_1 = '--current'
        dict_0 = {str_0: set_0, str_0: set_1, str_1: set_1}
        parser_0 = module_0.Parser(dict_0)
        var_0 = parser_0.__repr__()

if __name__ == "__main__":
    unittest.main()
