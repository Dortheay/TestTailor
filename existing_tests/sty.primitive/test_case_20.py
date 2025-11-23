import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = 'rules'
            register_0 = module_0.Register()
            dict_0 = register_0.as_dict()
            bytes_0 = None
            str_1 = '\nA selection of render functions.\n\nThese functions generate the escape-sequences that trigger certain colors/effects in\nthe terminals.\n'
            list_0 = None
            list_1 = [str_1, str_1, bytes_0]
            dict_1 = register_0.as_dict()
            register_1 = module_0.Register()
            tuple_0 = (bytes_0, str_1, list_0, list_1)
            type_0 = None
            str_2 = 'T$Z'
            dict_2 = {str_2: tuple_0, str_0: dict_0}
            register_0.set_renderfunc(type_0, dict_2)
            style_0 = module_0.Style()
            register_2 = module_0.Register()
            register_3 = register_2.copy()
            var_0 = register_3.__setattr__(str_0, style_0)
            register_3.set_renderfunc(str_0, tuple_0)
            register_4 = module_0.Register()
            register_0.set_eightbit_call(type_0)
            register_5 = module_0.Register()
            int_0 = 30
            str_3 = ',\\<e"U]'
            var_1 = register_5.as_namedtuple()
            list_2 = [int_0, str_3, int_0]
            str_4 = register_5.__call__(*list_2)
            int_1 = 588
            str_5 = '(WL1<:XKr'
            style_1 = style_0.__new__(int_1, value=str_5)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
