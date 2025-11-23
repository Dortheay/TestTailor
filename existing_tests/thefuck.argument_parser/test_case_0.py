import unittest
import timeout_decorator
import thefuck.argument_parser as module_0

class Test_Argument_parser_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        parser_0 = module_0.Parser()

if __name__ == "__main__":
    unittest.main()
