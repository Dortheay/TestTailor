import unittest
import timeout_decorator
import thefuck.argument_parser as module_0

class Test_Argument_parser_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'uK2#\x0cs'
            parser_0 = module_0.Parser()
            var_0 = parser_0.parse(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
