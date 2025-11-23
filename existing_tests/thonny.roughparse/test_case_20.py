import unittest
import timeout_decorator
import thonny.roughparse as module_0

class Test_Roughparse_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            int_0 = 2170
            float_0 = 0.7
            rough_parser_0 = module_0.RoughParser(int_0, float_0)
            list_0 = [float_0, float_0]
            hyper_parser_0 = module_0.HyperParser(rough_parser_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
