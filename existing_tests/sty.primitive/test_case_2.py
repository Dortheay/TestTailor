import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        int_0 = -3375
        list_0 = [int_0]
        register_0 = module_0.Register()
        register_1 = register_0.copy()
        register_2 = register_1.copy()
        register_3 = register_2.copy()
        register_4 = register_3.copy()
        register_5 = register_4.copy()
        register_6 = register_5.copy()
        str_0 = register_6.__call__(*list_0)

if __name__ == "__main__":
    unittest.main()
