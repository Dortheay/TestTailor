import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'rules'
        register_0 = module_0.Register()
        dict_0 = register_0.as_dict()
        register_1 = module_0.Register()
        register_1.unmute()
        style_0 = module_0.Style()
        register_2 = module_0.Register()
        register_3 = register_2.copy()
        var_0 = register_3.__setattr__(str_0, style_0)
        register_4 = register_1.copy()
        register_5 = register_3.copy()
        int_0 = 30
        str_1 = ',\\<e"U]'
        var_1 = register_5.as_namedtuple()
        list_0 = [int_0, str_1, int_0]
        str_2 = register_5.__call__(*list_0)
        register_6 = register_0.copy()
        register_7 = module_0.Register()
        register_8 = module_0.Register()
        register_9 = module_0.Register()
        register_9.mute()

if __name__ == "__main__":
    unittest.main()
