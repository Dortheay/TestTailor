import unittest
import timeout_decorator
import blib2to3.pgen2.tokenize as module_0
import blib2to3.pgen2.grammar as module_1

class Test_Tokenize_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            callable_0 = None
            module_0.tokenize(callable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
