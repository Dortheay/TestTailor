import unittest
import timeout_decorator
import sty.primitive as module_0

class Test_Primitive_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        register_0 = module_0.Register()
        var_0 = register_0.as_namedtuple()

if __name__ == "__main__":
    unittest.main()
