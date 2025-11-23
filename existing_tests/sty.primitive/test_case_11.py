import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        register_0 = module_0.Register()
        str_0 = 'DAM=ozv>A1'
        register_1 = module_0.Register()
        dict_0 = register_1.as_dict()
        register_0.unmute()
        bytes_0 = None
        str_1 = '\nA selection of render functions.\n\nThese functions generate the escape-sequences that trigger certain colors/effects in\nthe terminals.\n'
        list_0 = None
        list_1 = [str_1, str_1, bytes_0]
        tuple_0 = (bytes_0, str_1, list_0, list_1)
        type_0 = None
        dict_1 = {bytes_0: register_0}
        register_0.set_renderfunc(type_0, dict_1)
        style_0 = module_0.Style()
        register_2 = register_0.copy()
        var_0 = register_2.__setattr__(str_0, style_0)
        register_2.set_renderfunc(str_0, tuple_0)
        register_3 = module_0.Register()
        register_4 = module_0.Register()
        int_0 = 30
        str_2 = 'vG2$'
        var_1 = register_4.as_namedtuple()
        list_2 = [int_0, str_2, int_0]
        str_3 = register_4.__call__(*list_2)
        str_4 = register_4.__call__()
        register_2.set_rgb_call(type_0)
        str_5 = '1E\\\t\twI\rh<7'
        var_2 = register_1.__setattr__(str_5, style_0)
        register_5 = register_2.copy()
        register_6 = module_0.Register()
        register_7 = module_0.Register()
        register_8 = module_0.Register()
        register_8.mute()

if __name__ == "__main__":
    unittest.main()
