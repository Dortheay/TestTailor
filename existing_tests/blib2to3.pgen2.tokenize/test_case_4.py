import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xb2\xbe\x9b\xa9%\xa4\xa9\xfc/\xa0ws'
            float_0 = -1277.77142
            var_0 = None
            list_0 = [var_0, float_0, bytes_0]
            dict_0 = {}
            token_error_0 = module_0.TokenError(*list_0, **dict_0)
            iterator_0 = module_0.generate_tokens(token_error_0, dict_0)
            float_1 = -1501.59575
            list_1 = []
            var_1 = module_0.printtoken(bytes_0, float_0, iterator_0, float_1, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
