import unittest
import timeout_decorator
import flutils.objutils as module_0

class Test_Objutils_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'e"uH;DcI*+cpet)dX'
        bool_0 = module_0.has_any_callables(str_0)

if __name__ == "__main__":
    unittest.main()
