import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            str_0 = '2zl.=2iLdjf'
            bool_0 = False
            option_parser_0 = module_0.OptionParser()
            option_parser_0.define(str_0, str_0, bool_0)
            str_1 = '}h,NqY%\n]1P/0'
            bool_1 = option_parser_0.__contains__(str_1)
            mockable_0 = module_0._Mockable(option_parser_0)
            mockable_0.__setattr__(str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
