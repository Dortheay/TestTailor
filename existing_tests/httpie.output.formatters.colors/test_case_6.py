import unittest
import timeout_decorator
import httpie.context as module_0
import httpie.output.formatters.colors as module_1

class Test_Colors_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'A0pmCqJ'
            optional_0 = module_1.get_lexer(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
