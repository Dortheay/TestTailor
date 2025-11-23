import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            dict_0 = {}
            tuple_0 = module_0.detect_encoding(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
