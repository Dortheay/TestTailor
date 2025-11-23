import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = 'rules'
        register_0 = module_0.Register()
        style_0 = module_0.Style()
        register_1 = module_0.Register()
        register_2 = register_1.copy()
        var_0 = register_2.__setattr__(str_0, style_0)
        register_3 = module_0.Register()
        register_4 = module_0.Register()
        int_0 = 30
        str_1 = ',\\<e"U]'
        var_1 = register_4.as_namedtuple()
        list_0 = [int_0, str_1, int_0]
        str_2 = register_4.__call__(*list_0)

if __name__ == "__main__":
    unittest.main()
