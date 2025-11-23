import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'Ht~+)sb4F{cF?}\x0c}=*Qe'
            list_0 = [str_0]
            style_0 = module_0.Style()
            register_0 = module_0.Register()
            register_1 = register_0.copy()
            var_0 = register_1.__setattr__(str_0, style_0)
            style_1 = module_0.Style(*list_0)
            register_2 = module_0.Register()
            register_3 = register_2.copy()
            var_1 = register_3.__setattr__(str_0, style_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
