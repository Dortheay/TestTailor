import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0

class Test_Tokenize_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        int_0 = 32
        str_0 = 'N'
        tuple_0 = (int_0, str_0)
        list_0 = [tuple_0, tuple_0]
        untokenizer_0 = module_0.Untokenizer()
        untokenizer_0.compat(tuple_0, list_0)
        var_0 = module_0.maybe()

if __name__ == "__main__":
    unittest.main()
