import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            assign_0 = module_0.Assign()
            int_0 = 16
            str_0 = '?V|X<L\x0cr'
            parser_0 = module_1.Parser(int_0)
            parser_0.parse(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
