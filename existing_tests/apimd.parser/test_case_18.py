import unittest
import timeout_decorator
import ast as module_0
import apimd.parser as module_1
import collections.abc as module_2

class Test_Parser_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'qy'
            str_1 = module_1.doctest(str_0)
            str_2 = 'qy'
            str_3 = module_1.doctest(str_2)
            subscript_0 = module_0.Subscript()
            str_4 = ':,inZ%c;G+'
            str_5 = '\x0cq'
            str_6 = "z((lk\\/7'TjS~b^2?F("
            str_7 = '\rPQ+P4a6}J('
            str_8 = None
            dict_0 = {str_5: str_0, str_6: str_5, str_7: str_0, str_8: str_5}
            resolver_0 = module_1.Resolver(str_4, dict_0)
            a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
