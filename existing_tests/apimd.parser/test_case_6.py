import unittest
import timeout_decorator
import apimd.parser as module_0
import ast as module_1

class Test_Parser_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        float_0 = -1198.84874
        expr_0 = module_1.expr()
        list_0 = [expr_0]
        list_1 = [float_0, list_0, float_0]
        attribute_0 = module_1.Attribute(*list_1)
        str_0 = 'bR8p76y^IXc>*t\\E"!P'
        str_1 = '\ryb9I$Q<]sn[dD2'
        str_2 = 'Q'
        str_3 = '#}_dpoCc\r,]4Bvw'
        str_4 = 'E|#W^'
        str_5 = 'Mz?\to$q$K{\\p6x%Y'
        dict_0 = {str_0: str_0, str_1: str_2, str_2: str_3, str_4: str_5}
        resolver_0 = module_0.Resolver(str_0, dict_0, str_2)
        a_s_t_0 = resolver_0.visit_Attribute(attribute_0)

if __name__ == "__main__":
    unittest.main()
