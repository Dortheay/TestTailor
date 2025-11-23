import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            option_parser_0 = module_0.OptionParser()
            str_0 = 'LREriY=;`qksp '
            bool_0 = option_parser_0.__contains__(str_0)
            text_i_o_0 = None
            str_1 = 'CZb\nE\\UwmU6]p3uxgk'
            option_parser_1 = module_0.OptionParser()
            iterator_0 = option_parser_0.__iter__()
            mockable_0 = module_0._Mockable(option_parser_1)
            str_2 = '4H]i'
            list_0 = []
            option_0 = module_0._Option(str_2, list_0, str_1, bool_0, str_1, str_2, text_i_o_0)
            option_0.set(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
