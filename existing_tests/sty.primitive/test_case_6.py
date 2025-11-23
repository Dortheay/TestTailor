import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        register_0 = module_0.Register()
        register_0.unmute()

if __name__ == "__main__":
    unittest.main()
