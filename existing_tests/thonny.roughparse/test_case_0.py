import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = False
        float_0 = -1130.5
        rough_parser_0 = module_0.RoughParser(bool_0, float_0)

if __name__ == "__main__":
    unittest.main()
