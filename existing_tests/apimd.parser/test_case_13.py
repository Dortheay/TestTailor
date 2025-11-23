import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        import_from_0 = module_1.ImportFrom()
        list_0 = [import_from_0, import_from_0]
        constant_0 = module_1.Constant(*list_0)
        str_0 = ' yg'
        str_1 = '--current'
        str_2 = 'H*~*u/4={\'L4"'
        str_3 = 'Gkt'
        str_4 = '\\:6\tg'
        dict_0 = {str_0: str_0, str_0: str_1, str_1: str_2, str_3: str_4}
        str_5 = 'b-'
        resolver_0 = module_0.Resolver(str_0, dict_0, str_5)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)

if __name__ == "__main__":
    unittest.main()
