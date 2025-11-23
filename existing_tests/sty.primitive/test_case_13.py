import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            register_0 = module_0.Register()
            register_1 = register_0.copy()
            register_2 = register_1.copy()
            str_0 = 'nPjxmH0 4sbJa2:F&\n'
            list_0 = [register_1, register_1, register_1]
            style_0 = module_0.Style(*list_0)
            var_0 = register_1.__setattr__(str_0, style_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
