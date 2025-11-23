import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            constant_0 = module_0.Constant()
            str_0 = 'Load root: '
            str_1 = '#'
            dict_0 = {str_0: str_0, str_1: str_0}
            resolver_0 = module_1.Resolver(str_0, dict_0)
            a_s_t_0 = resolver_0.visit_Constant(constant_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
