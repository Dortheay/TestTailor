import unittest
import timeout_decorator
import thefuck.argument_parser as module_0

class Test_Argument_parser_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = -1154.42
            parser_0 = module_0.Parser()
            var_0 = parser_0.parse(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
