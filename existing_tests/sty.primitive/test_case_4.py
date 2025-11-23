import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        register_0 = module_0.Register()
        register_1 = register_0.copy()
        register_2 = register_1.copy()
        register_3 = register_2.copy()
        str_0 = '"*k\toQ6S\tn'
        callable_0 = None
        register_2.set_renderfunc(str_0, callable_0)
        register_3.mute()

if __name__ == "__main__":
    unittest.main()
