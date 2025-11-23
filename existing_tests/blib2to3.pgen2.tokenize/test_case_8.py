import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '`_0V'
            list_0 = []
            tuple_0 = (str_0, list_0)
            path_like_0 = None
            float_0 = -1593.739727
            iterator_0 = module_0.generate_tokens(float_0)
            bool_0 = None
            tuple_1 = (path_like_0, iterator_0, bool_0, path_like_0)
            list_1 = [tuple_0, tuple_0, tuple_1, tuple_1]
            str_1 = module_0.untokenize(list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
