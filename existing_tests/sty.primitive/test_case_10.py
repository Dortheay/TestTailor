import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        str_0 = 'rules'
        register_0 = module_0.Register()
        style_0 = module_0.Style()
        register_1 = module_0.Register()
        register_2 = register_1.copy()
        var_0 = register_2.__setattr__(str_0, style_0)
        register_3 = module_0.Register()
        var_1 = register_3.as_namedtuple()
        str_1 = register_0.__call__()
        register_1.unmute()
        register_4 = module_0.Register()
        register_5 = module_0.Register()
        register_6 = module_0.Register()
        register_2.mute()

if __name__ == "__main__":
    unittest.main()
