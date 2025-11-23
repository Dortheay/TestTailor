import unittest
import timeout_decorator
import httpie.output.formatters.colors as module_0
import httpie.context as module_1

class Test_Colors_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'k,k i1Mxd+O?ew4d1A4/'
        bool_0 = None
        optional_0 = module_0.get_lexer(str_0, bool_0)

if __name__ == "__main__":
    unittest.main()
