import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            style_0 = module_0.Style()
            register_0 = module_0.Register()
            register_1 = register_0.copy()
            register_2 = register_1.copy()
            register_3 = register_2.copy()
            register_4 = register_3.copy()
            register_5 = module_0.Register()
            register_3.set_eightbit_call(style_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
