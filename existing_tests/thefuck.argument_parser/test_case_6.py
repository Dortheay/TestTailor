import unittest
import timeout_decorator
import thefuck.argument_parser as module_0

class Test_Argument_parser_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            parser_0 = module_0.Parser()
            parser_1 = module_0.Parser()
            var_0 = parser_1.print_usage()
            str_0 = '--overwrite'
            var_1 = parser_1.print_help()
            var_2 = parser_1.parse(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
