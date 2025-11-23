import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        register_0 = module_0.Register()
        register_1 = register_0.copy()

if __name__ == "__main__":
    unittest.main()
