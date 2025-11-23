import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            option_parser_0 = module_0.OptionParser()
            str_0 = '/data/zhuxx/TIARA-study/codamosa/test-apps/tornado/tornado/log.py'
            option_parser_1 = module_0.OptionParser()
            bool_0 = option_parser_1.__contains__(str_0)
            dict_0 = option_parser_0.as_dict()
            str_1 = 'W?jTMviF#'
            option_parser_2 = module_0.OptionParser()
            mockable_0 = module_0._Mockable(option_parser_2)
            mockable_0.__delattr__(str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
