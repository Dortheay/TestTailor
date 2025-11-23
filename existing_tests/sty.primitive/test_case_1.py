import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        register_0 = module_0.Register()
        str_0 = register_0.__call__()

if __name__ == "__main__":
    unittest.main()
