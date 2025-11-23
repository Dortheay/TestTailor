import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            int_0 = 1118
            str_0 = 'tuI<'
            tuple_0 = (int_0, str_0)
            str_1 = ''
            untokenizer_0 = module_0.Untokenizer()
            untokenizer_0.compat(tuple_0, str_1)
            int_1 = -1782
            tuple_1 = (int_0, int_1)
            untokenizer_0.add_whitespace(tuple_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
