import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            list_0 = []
            var_0 = module_0.any(*list_0)
            str_0 = 'Us'
            bytes_0 = None
            list_1 = [bytes_0]
            tuple_0 = (str_0, list_1)
            untokenizer_0 = module_0.Untokenizer()
            str_1 = untokenizer_0.untokenize(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
