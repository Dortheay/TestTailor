import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            untokenizer_0 = module_0.Untokenizer()
            str_0 = '5)w(O.sf.2P'
            str_1 = untokenizer_0.untokenize(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
