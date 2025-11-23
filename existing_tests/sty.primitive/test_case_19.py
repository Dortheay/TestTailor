import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            register_0 = module_0.Register()
            dict_0 = register_0.as_dict()
            bytes_0 = None
            str_0 = '\nA selection of render functions.\n\nThese functions generate the escape-sequences that trigger certain colors/effects in\nthe terminals.\n'
            list_0 = None
            list_1 = [str_0, str_0, bytes_0]
            tuple_0 = (bytes_0, str_0, list_0, list_1)
            style_0 = module_0.Style()
            register_1 = module_0.Register()
            register_2 = register_1.copy()
            var_0 = register_2.__setattr__(str_0, style_0)
            register_2.set_renderfunc(str_0, tuple_0)
            register_3 = module_0.Register()
            var_1 = register_3.as_namedtuple()
            str_1 = register_3.__call__()
            register_3.unmute()
            style_1 = style_0.__new__(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
