import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        register_0 = module_0.Register()
        register_0.mute()

if __name__ == "__main__":
    unittest.main()
