import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0

class Test_Grammar_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = b'\x97\xf2\x91\x9a8)\xdbT\\_Or\x87\xc4\xd4\x01N\xde'
            grammar_0 = module_0.Grammar()
            grammar_0.loads(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
