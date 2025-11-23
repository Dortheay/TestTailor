import unittest
import timeout_decorator
import blib2to3.pgen2.literals as module_0
import re as module_1

class Test_Literals_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = "'hello'"
            str_1 = module_0.evalString(str_0)
            str_2 = "'world\\n'"
            str_3 = module_0.evalString(str_2)
            str_4 = "'escaped\\'quote\\''"
            str_5 = module_0.evalString(str_4)
            str_6 = "'tab\\tcharacter'"
            str_7 = module_0.evalString(str_6)
            str_8 = '"hello"'
            str_9 = module_0.evalString(str_8)
            str_10 = '"world\\n"'
            str_11 = module_0.evalString(str_10)
            str_12 = '"escaped\\"quote\\""'
            str_13 = module_0.evalString(str_12)
            str_14 = '"""multiline\nstring"""'
            str_15 = module_0.evalString(str_14)
            str_16 = "'hex\\x41'"
            str_17 = module_0.evalString(str_16)
            str_18 = "'hex\\x7F'"
            str_19 = module_0.evalString(str_18)
            str_20 = "'invalid\\xG1'"
            str_21 = module_0.evalString(str_20)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
