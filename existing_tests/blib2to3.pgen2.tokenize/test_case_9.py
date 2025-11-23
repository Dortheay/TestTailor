import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            callable_0 = None
            iterator_0 = module_0.generate_tokens(callable_0)
            tuple_0 = ()
            str_0 = module_0.untokenize(tuple_0)
            str_1 = module_0.untokenize(iterator_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
