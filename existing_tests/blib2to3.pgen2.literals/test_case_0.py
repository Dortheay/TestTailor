import unittest
import timeout_decorator
import blib2to3.pgen2.literals as module_0
import re as module_1

class Test_Literals_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = '\\"(r9"jP3nv1'
            str_1 = module_0.evalString(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
