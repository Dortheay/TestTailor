import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0

class Test_Tokenize_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        untokenizer_0 = module_0.Untokenizer()
        int_0 = -1835
        int_1 = 593
        tuple_0 = (int_0, int_1)
        untokenizer_0.add_whitespace(tuple_0)

if __name__ == "__main__":
    unittest.main()
