import unittest
import timeout_decorator
import blib2to3.pgen2.literals as module_0
import re as module_1

class Test_Literals_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = "'\\n\\t\\\\'"
            str_1 = module_0.evalString(str_0)
            str_2 = '"\\n\\t\\\\"'
            str_3 = module_0.evalString(str_2)
            str_4 = "'\\x41\\x42\\x43'"
            str_5 = module_0.evalString(str_4)
            str_6 = "'\\101\\102\\103'"
            str_7 = module_0.evalString(str_6)
            str_8 = '"""Hello\\nWorld"""'
            str_9 = module_0.evalString(str_8)
            str_10 = "''"
            str_11 = module_0.evalString(str_10)
            str_12 = "'\\x1'"
            str_13 = module_0.evalString(str_12)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
