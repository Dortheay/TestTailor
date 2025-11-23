import unittest
import timeout_decorator
import blib2to3.pgen2.grammar as module_0

class Test_Grammar_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'C8\x0b'
            grammar_0 = module_0.Grammar()
            grammar_0.load(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
