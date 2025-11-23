import unittest
import timeout_decorator
import blib2to3.pgen2.literals as module_0
import re as module_1

class Test_Literals_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = '\\\\(.)'
            str_1 = '\\\\n'
            var_0 = module_1.match(str_0, str_1)
            str_2 = module_0.escape(var_0)
            str_3 = '\\\\t'
            var_1 = module_1.match(str_0, str_3)
            str_4 = module_0.escape(var_1)
            str_5 = "\\\\'"
            var_2 = module_1.match(str_0, str_5)
            str_6 = module_0.escape(var_2)
            str_7 = '\\\\"'
            var_3 = module_1.match(str_0, str_7)
            str_8 = module_0.escape(var_3)
            str_9 = '\\\\\\\\'
            var_4 = module_1.match(str_0, str_9)
            str_10 = module_0.escape(var_4)
            str_11 = '\\\\(.)'
            str_12 = '\\\\x'
            var_5 = module_1.match(str_11, str_12)
            str_13 = module_0.escape(var_5)
            str_14 = '\\\\(.{2})'
            str_15 = '\\\\x41'
            var_6 = module_1.match(str_14, str_15)
            str_16 = module_0.escape(var_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
