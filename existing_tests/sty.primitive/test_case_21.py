import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            str_0 = 'rules'
            register_0 = module_0.Register()
            dict_0 = register_0.as_dict()
            list_0 = None
            style_0 = module_0.Style()
            register_1 = module_0.Register()
            register_2 = register_1.copy()
            var_0 = register_2.__setattr__(str_0, style_0)
            register_3 = module_0.Register()
            var_1 = register_3.as_namedtuple()
            str_1 = register_3.__call__()
            register_2.unmute()
            style_1 = style_0.__new__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
